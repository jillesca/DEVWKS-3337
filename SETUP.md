# Set the environment

This guide walks you through setting up your workshop environment, including SSH configuration and cloning the necessary repositories to both VMs.

## SSH Agent Prerequisites - Workshop Laptop

On the laptop provided, start the ssh agent and add the ssh keys.

```bash
eval "$(ssh-agent -s)"
```

```bash
ssh-add ~/.ssh/clus25_workshop_key
```

## Clone the repos

Credentials:

- **Username**: `root`
- **Password**: `C1sco12345`

You can use vscode (recommended) or the terminal client:

- `ssh root@198.18.134.28` - XRd host VM
- Workshop laptop - for the agent/tooling VM

> [!TIP]  
> vscode is recommended option for this workshop. It's already configured with access to both VMs.

### XRd VM - 198.18.134.28

On `198.18.134.28`, log in and run:

```bash
cd /root
git clone https://github.com/jillesca/XRd-Labs
```

### Workshop Laptop

On the workshop laptop run:

```bash
mkdir -p /home/devnet/DEVWKS-3337
cd /home/devnet/DEVWKS-3337
```

```bash
git clone https://github.com/jillesca/gNMIBuddy
```

```bash
git clone https://github.com/jillesca/sp_oncall
```

```bash
git clone https://github.com/jillesca/DEVWKS-3337
```

## Next Steps - Setting Up XRd

Once you've completed cloning all repositories, proceed to [Setup XRd](SETUP_XRd.md) to configure the virtual routers.
