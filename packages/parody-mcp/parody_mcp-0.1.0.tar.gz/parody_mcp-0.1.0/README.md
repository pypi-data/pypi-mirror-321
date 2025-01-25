# Parody Word Suggestion MCP Tool

This is an MCP tool that suggests funny, phonetically similar words using the CMU pronunciation dictionary.

## Installation

Install the package locally for development:
```bash
pip install -e .
```

## Usage

You can use this tool with smolagents like this:

```python
import os
from mcp import StdioServerParameters
from smolagents import CodeAgent, HfApiModel, ToolCollection

mcp_server_params = StdioServerParameters(
    command="uvx",
    args=["--quiet", "parody_mcp"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(mcp_server_params) as tool_collection:
    agent = CodeAgent(tools=tool_collection.tools, model=HfApiModel())
    agent.run("Find me funny words that sound like 'hamburger'")