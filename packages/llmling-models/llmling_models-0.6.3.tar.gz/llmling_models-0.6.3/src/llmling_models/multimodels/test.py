"""Callback-based model selection."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import Field, ImportString
from pydantic_ai.models import AgentModel, Model

from llmling_models.log import get_logger
from llmling_models.multi import MultiModel


if TYPE_CHECKING:
    from pydantic_ai.tools import ToolDefinition


logger = get_logger(__name__)


class CallbackMultiModel(MultiModel[Model]):
    """Multi-model using a callback for selection."""

    type: Literal["callback"] = Field(default="callback", init=False)
    selector: ImportString[Model]
    """Import path to selection function that returns a Model"""

    def name(self) -> str:
        """Get descriptive model name."""
        return f"callback({len(self.models)})"

    async def agent_model(
        self,
        *,
        function_tools: list[ToolDefinition],
        allow_text_result: bool,
        result_tools: list[ToolDefinition],
    ) -> AgentModel:
        """Create agent model from selected model."""
        # Get the last prompt from the tools context if available
        prompt = ""  # TODO: How do we get the prompt here?

        # Select model based on prompt
        selected = self.selector(self.available_models, prompt)

        return await selected.agent_model(
            function_tools=function_tools,
            allow_text_result=allow_text_result,
            result_tools=result_tools,
        )


if __name__ == "__main__":
    import asyncio

    from pydantic_ai import Agent

    async def test():
        model = CallbackMultiModel(
            models=["openai:gpt-4", "openai:gpt-3.5-turbo"],
            selector="my_package.selectors:select_by_complexity",
        )
        agent: Agent[None, str] = Agent(model=model)
        result = await agent.run("What is the meaning of life?")
        print(result.data)

    asyncio.run(test())
