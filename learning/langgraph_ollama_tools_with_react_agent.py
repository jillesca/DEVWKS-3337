"""
This example demonstrates using LangGraph's ReAct agent with Ollama models.

The example shows how to:
1. Create a simple tool (add function)
2. Set up a ReAct agent using LangGraph
3. Execute the agent with a basic math query

Tested with Ollama version 0.6.6 and the following models:
- llama3.1
- qwen3:8b

Tested with:
- langchain >= 0.3.24
- langchain-ollama >= 0.3.2
- langgraph >= 0.4.1
- ollama >= 0.4.8
- Python >= 3.10

Setup instructions:
1. Install Ollama from https://ollama.com/ (version 0.6.6 or later)
2. Pull a compatible model: `ollama pull llama3.1` or `ollama pull qwen3:8b`
3. Run this script with Python 3.10 or later

Notes:
- ReAct (Reasoning + Acting) agents combine reasoning and tool use in an interleaved manner
- LangGraph simplifies the creation of agents with structured reasoning workflows
- The temperature is set to 0 for deterministic responses, adjust as needed for creativity
- You can add more tools by creating additional functions with the @tool decorator
"""

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


@tool
def add(x: int, y: int) -> int:
    """Adds 2 numbers and returns the result"""
    return x + y


tools = [add]

LLM = "qwen3:8b"

model = ChatOllama(
    model=LLM,
    temperature=0,
)

prompt = "You are a helpful assistant, always use the tools provided to answer the user's question."
messages = {
    "messages": [{"role": "user", "content": "use the add tool to add 2 + 2"}]
}

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=prompt,
)

# Run the agent
answer = agent.invoke(messages)
print(answer)
