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
