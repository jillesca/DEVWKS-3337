```bash
npx @modelcontextprotocol/inspector \
uv run --with "mcp[cli],pygnmi,networkx" \
mcp run /Users/jillesca/DevNet/cisco_live/25clus/gNMIBuddy/mcp_server.py
```

```bash
uv run --with "mcp[cli],pygnmi,networkx" \
    /Users/jillesca/DevNet/cisco_live/25clus/gNMIBuddy/cli_app.py \
    --inventory /Users/jillesca/DevNet/cisco_live/25clus/DEVWKS-3337/xrd_inventory.json \
    --device xrd-1 \
    mpls \
    --detail
```

```bash
git clone --branch release git@github.com:jillesca/sp_oncall.git
git clone --branch release https://github.com/jillesca/sp_oncall.git
git clone --branch release git@github.com:jillesca/gNMIBuddy.git
git clone --branch release https://github.com/jillesca/gNMIBuddy.git
git clone --branch release git@github.com:jillesca/XRd-Labs.git
git clone --branch release git@github.com:jillesca/DEVWKS-3337.git
```

Working directory:

```bash
/home/devnet/DEVWKS-3337
~/DEVWKS-3337
/home/devnet/DEVWKS-3337/gNMIBuddy
```
