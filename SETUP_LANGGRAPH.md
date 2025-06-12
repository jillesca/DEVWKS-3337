# Setup Langgraph - Workshop Laptop

Follow these steps on your **Workshop Laptop**.

## 1. Open the Project

Open the `sp_oncall` project in VSCode.

## 2. Set Environment Variables

Create a `.env` file in the root directory of the `sp_oncall` project (`/home/devnet/DEVWKS-3337/sp_oncall/.env`) with the following environment variables:

```bash
# .env file
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
OPENAI_API_KEY=<OPENAI_API_KEY>           # Provided at the workshop or use your own
LANGSMITH_PROJECT=<ws1-seatID>            # Replace with your workshop seat ID (e.g., ws1-seat42)
LANGSMITH_API_KEY=<LANGSMITH_API_KEY>     # Get from https://smith.langchain.com/ (see below)
```

- Use the `OPENAI_API_KEY` provided at the workshop, or your own.
- For `LANGSMITH_API_KEY`, log in to <https://smith.langchain.com/> and create your own key (credentials provided at the workshop too).
- Make sure to switch to the `DEVWKS-3337` organization used by the workshop.

> [!IMPORTANT]
> All environment variables **are required**. If any are missing, Langgraph will fail to start.

## 3. Start Langgraph

Start the langgraph server using the prepared Makefile command. This will initialize the agents that will interact with your network.

```bash
cd /home/devnet/DEVWKS-3337/sp_oncall && make run
```

## 4. Verify Langgraph Setup

After the server starts, Langgraph will redirect to a web app where you can interact with the graph you just started. You'll see the Langgraph UI where you can interact with the network agents.

- The graph expects you to provide the hostname of a device present in the inventory file. The inventory file is located at the root of the project under `/xrd_inventory.json`.
- Start with a simple query to verify everything is working correctly. For example: _"how is xrd-8 configured?"_

If you see results, your setup is working!

## 5. Add MCP Support

Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs.

We need to add tools to the Langgraph agents to interact with the network. We will use MCP to connect the agent with gNMIBuddy.

### 5.1 Test Tools on the Workshop Laptop

In another terminal on your **Workshop Laptop**, test the tools using the [MCP Inspector tool](https://modelcontextprotocol.io/docs/tools/inspector). This tool allows you to inspect and run MCP tools locally.

```bash
npx @modelcontextprotocol/inspector \
uv run --with "mcp[cli],pygnmi,networkx" \
mcp run /home/devnet/DEVWKS-3337/gNMIBuddy/mcp_server.py
```

- In the MCP Inspector, set the environment variable:

```bash
NETWORK_INVENTORY
```

to:

```bash
/home/devnet/DEVWKS-3337/DEVWKS-3337/xrd_inventory.json
```

### 5.2 Add MCP Configuration to Langgraph

On Langgraph, add the MCP configuration to the `sp_oncall` project. This will allow the agents to use the gNMIBuddy tool.

- In the _Manage Assistants_ setting, add the following configuration to the `Mcp Client Config` field:

```json
{
  "gNMIBuddy": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "mcp[cli],pygnmi,networkx",
      "mcp",
      "run",
      "/home/devnet/DEVWKS-3337/gNMIBuddy/mcp_server.py"
    ],
    "transport": "stdio",
    "env": {
      "NETWORK_INVENTORY": "/home/devnet/DEVWKS-3337/DEVWKS-3337/xrd_inventory.json"
    }
  }
}
```

- Close the settings and test your query again. This time the agent should be able to use the gNMIBuddy tool to answer your question.
