import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aws_cdk import App, Stack
from aws_cdk import aws_s3 as s3
from models import create_agent_with_tools
from langchain_core.messages import SystemMessage
from parser import CDKStackParser
from codegen.extensions.langchain.tools import (
    ListDirectoryTool,
    RevealSymbolTool,
    SearchTool,
    SemanticSearchTool,
    ViewFileTool,
)

RESEARCH_AGENT_PROMPT = """You are a code research expert. Your goal is to help users understand codebases by:
1. Finding relevant code through semantic and text search
2. Analyzing symbol relationships and dependencies
3. Exploring directory structures
4. Reading and explaining code

Always explain your findings in detail and provide context about how different parts of the code relate to each other.
When analyzing code, consider:
- The purpose and functionality of each component
- How different parts interact
- Key patterns and design decisions
- Potential areas for improvement

Break down complex concepts into understandable pieces and use examples when helpful."""


def main():

    # initialize the codebase starting directory
    parser= CDKStackParser()
    codebase = parser.initialize_parser("/Users/shikagg/migration_tool/example_stack1")
    # Create research tools
    tools = [
    ViewFileTool(codebase),      # View file contents
    ListDirectoryTool(codebase),  # Explore directory structure
    SearchTool(codebase),        # Text-based search
    SemanticSearchTool(codebase), # Natural language search
    RevealSymbolTool(codebase),  # Analyze symbol relationships
    ]

    # Initialize the agent
    agent = create_agent_with_tools(
    codebase=codebase,
    tools=tools,
    chat_history=[SystemMessage(content=RESEARCH_AGENT_PROMPT)],
    verbose=True)

if __name__ == "__main__":
    main()
