"""FastAPI server for remote human-in-the-loop conversations."""

from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, datetime
from typing import Any, Literal

from fastapi import FastAPI, Header, HTTPException, WebSocket, WebSocketDisconnect, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from pydantic_ai.messages import (
    ModelMessage,
    ModelMessagesTypeAdapter,
    ModelResponse,
    TextPart,
)
from pydantic_ai.usage import Usage

from llmling_models.log import get_logger


logger = get_logger(__name__)
security = HTTPBearer()


class Message(BaseModel):
    """Single conversation message."""

    role: Literal["user", "assistant"]
    content: str


class CompletionRequest(BaseModel):
    """Request for completion."""

    prompt: str
    conversation: list[Message] | None = None


class CompletionResponse(BaseModel):
    """Response from completion."""

    content: str


class StreamResponse(BaseModel):
    """Streaming response chunk."""

    chunk: str
    done: bool = False
    error: str | None = None


def format_conversation(messages: list[ModelMessage]) -> str:
    """Format conversation for display to operator."""
    lines = []

    # Format history
    for message in messages[:-1]:
        prefix = "🤖" if isinstance(message, ModelResponse) else "👤"
        formatted_lines = [
            f"{prefix} {part.content}"  # type: ignore
            for part in message.parts
            if hasattr(part, "content")
        ]
        lines.extend(formatted_lines)

    # Format current prompt
    if messages:
        last_message = messages[-1]
        for part in last_message.parts:
            if hasattr(part, "content"):
                lines.append("\n>>> Current prompt:")
                lines.append(f"👤 {part.content}")  # type: ignore
                lines.append("\nYour response: ")

    return "\n".join(lines)


class ModelServer:
    """Server that delegates to human operator."""

    def __init__(self, title: str = "Input Server", description: str | None = None):
        """Initialize server with configuration."""
        self.app = FastAPI(title=title, description=description or "No description")
        self._setup_routes()

    def _setup_routes(self):
        """Configure API routes."""

        @self.app.post("/v1/completion")
        async def create_completion(
            messages: list[ModelMessage],
            auth: str = Header(..., alias="Authorization"),
        ) -> dict[str, Any]:
            """Handle completion requests via REST."""
            try:
                # Display conversation to operator
                print("\n" + "=" * 80)
                print(format_conversation(messages))
                print("-" * 80)
                response_text = input("Your response: ").strip()

                # Create model response
                response = ModelResponse(
                    parts=[TextPart(response_text)],
                    timestamp=datetime.now(UTC),
                )
                # Return with empty usage stats
                return {
                    "content": str(response.parts[0].content),  # type: ignore
                    "usage": asdict(Usage()),
                }

            except Exception as e:
                logger.exception("Error processing completion request")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=str(e),
                ) from e

        @self.app.websocket("/v1/completion/stream")
        async def websocket_endpoint(websocket: WebSocket):
            """Handle streaming conversation via WebSocket."""
            await websocket.accept()

            try:
                while True:
                    # Receive and parse messages
                    raw_data = await websocket.receive_text()
                    messages = ModelMessagesTypeAdapter.validate_json(raw_data)

                    # Display to operator
                    print("\n" + "=" * 80)
                    print(format_conversation(messages))
                    print("-" * 80)

                    # Get response character by character
                    print("Type your response (press Enter when done):")
                    buffer = []
                    while True:
                        char = input()  # This is synchronous - for demo only
                        if not char:  # Enter pressed
                            break

                        buffer.append(char)
                        # Send character as stream chunk
                        await websocket.send_json({
                            "chunk": char,
                            "done": False,
                        })

                    # Send completion
                    await websocket.send_json({
                        "chunk": "",
                        "done": True,
                        "usage": asdict(Usage()),
                    })

            except WebSocketDisconnect:
                logger.info("WebSocket disconnected")

    def run(self, host: str = "0.0.0.0", port: int = 8000, **kwargs: Any):
        """Start the server."""
        import uvicorn

        uvicorn.run(self.app, host=host, port=port, **kwargs)


if __name__ == "__main__":
    import logging

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    server = ModelServer(
        title="Remote Input Server",
        description="Server that delegates to human operator",
    )
    server.run(port=8000)
