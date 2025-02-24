import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from langgraph.prebuilt import create_react_agent
from langchain.tools import BaseTool
from langchain_core.messages import SystemMessage
from langgraph.graph.graph import CompiledGraph
from langgraph.checkpoint.memory import MemorySaver
from llm import LLM
from prompts import REASONER_SYSTEM_MESSAGE


## create custom agent with tool
def create_agent_with_tools(
    tools: list[BaseTool],
    model_provider: str = "",
    model_name: str = "gpt-4o",
    system_message: SystemMessage = SystemMessage(REASONER_SYSTEM_MESSAGE),
    memory: bool = True,
    debug: bool = True,
    **kwargs,
) -> CompiledGraph:
    """Create an agent with a specific set of tools.

    Args:
        codebase: The codebase to operate on
        tools: List of tools to provide to the agent
        model_provider: The model provider to use ("anthropic" or "openai")
        model_name: Name of the model to use
        system_message: Custom system message to use (defaults to standard reasoner message)
        memory: Whether to enable memory/checkpointing
        **kwargs: Additional LLM configuration options. Supported options:
            - temperature: Temperature parameter (0-1)
            - top_p: Top-p sampling parameter (0-1)
            - top_k: Top-k sampling parameter (>= 1)
            - max_tokens: Maximum number of tokens to generate

    Returns:
        Compiled langgraph agent
    """

    llm = LLM(
        model_provider=model_provider,
        model_name=model_name,
        **kwargs
    )

    memory = MemorySaver() if memory else None

    return create_react_agent(model=llm, tools=tools, prompt=system_message, checkpointer=memory, debug=debug)