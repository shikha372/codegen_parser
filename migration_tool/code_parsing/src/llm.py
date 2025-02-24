"""LLM implementation using Amazon Bedrock."""

from collections.abc import Sequence
from typing import Any, Optional

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatResult
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from langchain_aws import ChatBedrock
from pydantic import Field

class LLM(BaseChatModel):
    """A chat model using Amazon Bedrock."""

    model_id: str = Field(
        default="anthropic.claude-3-sonnet-20240229-v1:0",
        description="The Bedrock model ID to use."
    )

    temperature: float = Field(
        default=0,
        description="Temperature parameter for the model.",
        ge=0,
        le=1
    )

    max_tokens: Optional[int] = Field(
        default=None,
        description="Maximum number of tokens to generate.",
        ge=1
    )

    def __init__(self, model_id: str = "anthropic.claude-3-sonnet-20240229-v1:0", **kwargs: Any) -> None:
        """Initialize the LLM.

        Args:
            model_id: The Bedrock model ID to use
            **kwargs: Additional configuration options. Supported options:
                - temperature: Temperature parameter (0-1)
                - max_tokens: Maximum number of tokens to generate
        """
        kwargs["model_id"] = model_id

        # Filter out unsupported kwargs
        supported_kwargs = {"model_id", "temperature", "max_tokens", "callbacks", "tags", "metadata"}
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in supported_kwargs}

        super().__init__(**filtered_kwargs)
        self._model = self._get_model()

    @property
    def _llm_type(self) -> str:
        """Return identifier for this LLM class."""
        return "bedrock_chat_model"

    def _get_model_kwargs(self) -> dict[str, Any]:
        """Get kwargs for the Bedrock model."""
        model_kwargs = {"temperature": self.temperature}
        
        if self.max_tokens is not None:
            model_kwargs["max_tokens"] = self.max_tokens

        return {
            "model_id": self.model_id,
            "model_kwargs": model_kwargs
        }

    def _get_model(self) -> BaseChatModel:
        """Get the ChatBedrock model instance."""
        return ChatBedrock(**self._get_model_kwargs())

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: Optional[list[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Generate chat completion using the Bedrock model.

        Args:
            messages: The messages to generate from
            stop: Optional list of stop sequences
            run_manager: Optional callback manager for tracking the run
            **kwargs: Additional arguments to pass to the model

        Returns:
            ChatResult containing the generated completion
        """
        return self._model._generate(messages, stop=stop, run_manager=run_manager, **kwargs)

    def bind_tools(
        self,
        tools: Sequence[BaseTool],
        **kwargs: Any,
    ) -> Runnable[LanguageModelInput, BaseMessage]:
        """Bind tools to the underlying model.

        Args:
            tools: List of tools to bind
            **kwargs: Additional arguments to pass to the model

        Returns:
            Runnable that can be used to invoke the model with tools
        """
        return self._model.bind_tools(tools, **kwargs)
