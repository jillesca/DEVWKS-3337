# Setup Langgraph - Workshop Laptop

## Set environment variables

Create a `.env` file in the root directory of the `sp_oncall` project (`/home/devnet/DEVWKS-3337/sp_oncall/.env`) with the following environment variables:

```bash
# .env file
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
OPENAI_API_KEY=<OPEN_API_KEY>
LANGSMITH_PROJECT=<ws1-seatID>   # Replace with your workshop seat ID (example: ws1-seat42)
LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
```

Use the `OPENAI_API_KEY` provided at the workshop, or use your own.

For `LANGSMITH_API_KEY` login to <https://smith.langchain.com/> and create you own key (credentials provided at the workshop too).

Make sure to switch to the `DEVWKS-3337` organization used by the workshop.

> [!IMPORTANT]  
> All environment variables **are required**, otherwise the Langgraph will fail.

## Start Langgraph

Start the langgraph server using the prepared Makefile command. This will initialize the agents that will interact with your network.

```bash
cd /home/devnet/DEVWKS-3337/sp_oncall && make run
```

### Verifying Langgraph Setup

After the server starts, langgraph redirects to a web app where we can interact with the graph we just started. You'll see the Langgraph UI where you can interact with the network agents.

Start with a simple query to verify everything is working correctly. For example, "how is xrd-8 configured?".

How the results were?

## Add MCP Support

We need to add tools to the Langgraph agents to interact with the network. We will use MCP to connect the agent with gNMIBuddy.

### Test tools on the workshop laptop

To test the tools on the workshop laptop, we will use the [MCP Inspector tool](https://modelcontextprotocol.io/docs/tools/inspector). This tool allows us to inspect and run MCP tools locally.

```bash
npx @modelcontextprotocol/inspector \
uv run --with "mcp[cli],pygnmi,networkx" \
mcp run /home/devnet/DEVWKS-3337/gNMIBuddy/mcp_server.py
```

> [!NOTE]  
> On the MCP inspector set the environment variable `NETWORK_INVENTORY` to `/home/devnet/DEVWKS-3337/xrd_inventory.json`.

### Add MCP configuration

On Langgraph, we need to add the MCP configuration to the `sp_oncall` project. This will allow the agents to use the gNMIBuddy tool.

On the _Manage Assistants_ setting, add the following configuration to the `Mcp Client Config` field:

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
      "NETWORK_INVENTORY": "/home/devnet/DEVWKS-3337/xrd_inventory.json"
    }
  }
}
```

Close the settings and test your query again. This time the agent should be able to use the gNMIBuddy tool to answer your question.
