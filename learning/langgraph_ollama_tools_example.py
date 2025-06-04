"""
This example demonstrates using Ollama models with LangChain tools.

The example shows how to:
1. Create a simple tool (add function)
2. Bind tools to an Ollama model
3. Execute the model with a basic math query
4. Handle tool calls and responses manually

Tested with Ollama version 0.6.6 and the following models:
- llama3.1
- qwen3:8b

Tested with:
- langchain >= 0.3.24
- langchain-ollama >= 0.3.2
- ollama >= 0.4.8
- Python >= 3.10

Setup instructions:
1. Install Ollama from https://ollama.com/ (version 0.6.6 or later)
2. Pull a compatible model: `ollama pull llama3.1` or `ollama pull qwen3:8b`
3. Run this script with Python 3.10 or later

Notes:
- This example shows the manual approach to tool calling without using agent frameworks
- The temperature is set to 0 for deterministic responses, adjust as needed for creativity
- You may need to adjust the handling of tool calls based on the specific model used
- This approach gives you more control over each step in the tool-calling process
- For a more structured approach with less boilerplate, see the ReAct agent example
"""

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage


@tool
def add(x: int, y: int) -> int:
    """Adds 2 numbers and returns the result"""
    return x + y


tools = [add]

LLM = "qwen3:8b"

model = ChatOllama(
    model=LLM,
    temperature=0,
).bind_tools(tools)

messages = [
    SystemMessage(
        content="You are a helpful assistant, always use the tools provided to answer the user's question."
    ),
    HumanMessage(content="use the add tool to add 2 + 2"),
]

# First model call - will likely get a tool call
response = model.invoke(messages)
print(f"Initial response: {response}")

# Check for tool calls
if response.tool_calls:
    # Loop through each tool call
    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_id = tool_call["id"]

        # Find the matching tool
        for tool in tools:
            if tool.name == tool_name:
                # Execute the tool with the arguments
                tool_result = tool.invoke(tool_args)
                print(f"Tool result: {tool_result}")

                # Add the tool result to the messages
                messages.append(response)
                messages.append(
                    ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_id,
                        name=tool_name,
                    )
                )

                # Get final response after tool execution
                final_response = model.invoke(messages)
                print(f"Final response: {final_response.content}")
                break
else:
    print("No tool calls were made.")
