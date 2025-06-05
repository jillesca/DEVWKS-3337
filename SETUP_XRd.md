# XRd containers

## XRd Credentials

- **Username**: `admin`
- **Password**: `C1sco123`

## Devices

The following table lists the devices and their corresponding IP addresses:

| **Device Name** | **IP Address** |
| --------------- | -------------- |
| `xrd-1`         | 198.18.158.16  |
| `xrd-2`         | 198.18.158.17  |
| `xrd-3`         | 198.18.158.18  |
| `xrd-4`         | 198.18.158.19  |
| `xrd-5`         | 198.18.158.20  |
| `xrd-6`         | 198.18.158.21  |
| `xrd-7`         | 198.18.158.22  |
| `xrd-8`         | 198.18.158.23  |
| `xrd-9`         | 198.18.158.24  |
| `xrd-10`        | 198.18.158.25  |

## Network Topology

The diagram below illustrates the network topology for this project:

```plaintext
                 xrd-7 (PCE)
                 /        \
              xrd-3 --- xrd-4
               / |        | \
xrd-9 --- xrd-1  |        |  xrd-2 --- xrd-10
               \ |        | /
              xrd-5 --- xrd-6
                 \        /
                 xrd-8 (vRR)
```

## 🧪 Lab Setup Instructions

On `198.18.134.28`.

### Host Verification - 198.18.134.28

Verify the host VM meets the requirements needed by XRd control plane.

```bash
/root/xrd-tools/scripts/host-check --platform xrd-control-plane --extra-checks docker --extra-checks xr-compose
```

<details>
<summary>Expected Output</summary>

```bash
root@xrd-host:~# /root/xrd-tools/scripts/host-check --platform xrd-control-plane --extra-checks docker --extra-checks xr-compose
==============================
Platform checks - xrd-control-plane
==============================
PASS -- CPU architecture (x86_64)
PASS -- CPU cores (16)
PASS -- Kernel version (5.4)
PASS -- Base kernel modules
        Installed module(s): dummy, nf_tables
PASS -- Cgroups (v1)
PASS -- Inotify max user instances
        64000 - this is expected to be sufficient for 16 XRd instance(s).
PASS -- Inotify max user watches
        64000 - this is expected to be sufficient for 16 XRd instance(s).
PASS -- Socket kernel parameters (valid settings)
PASS -- UDP kernel parameters (valid settings)
INFO -- Core pattern (core files managed by the host)
PASS -- ASLR (full randomization)
WARN -- Linux Security Modules
        AppArmor is enabled. XRd is currently unable to run with the
        default docker profile, but can be run with
        '--security-opt apparmor=unconfined' or equivalent.
        However, some features might not work, such as ZTP.
PASS -- RAM
        Available RAM is 7.9 GiB.
        This is estimated to be sufficient for 3 XRd instance(s), although memory
        usage depends on the running configuration.
        Note that any swap that may be available is not included.

==============================
Extra checks
==============================

xr-compose checks
-----------------------
PASS -- docker-compose (version 1.25.0)
PASS -- PyYAML (installed)
PASS -- Bridge iptables (disabled)

==================================================================
!! Host NOT set up correctly for xrd-control-plane !!
------------------------------------------------------------------
Extra checks passed: xr-compose
==================================================================
root@xrd-host:~#
```

</details>

Verify the XRd image is present on the VM.

```bash
docker image ls
```

Review the existing containers.

```bash
docker ps -a
```

### Prepare XRd Instances - 198.18.134.28

On the XRd host (198.18.134.28) convert the xr-compose file into a docker compose file.

```bash
xr-compose \
  --input-file ~/XRd-Labs/clus25-devwks3337/docker-compose.xr.yml \
  --output-file ~/XRd-Labs/clus25-devwks3337/docker-compose.yml \
  --image ios-xr/xrd-control-plane:24.2.1
```

Since we are using macvlan mode on docker, we need to tell the XRd containers which container interface will be map to the XRd management interface.

```bash
sed -i 's/XR_MGMT_INTERFACES: linux:xr-[0-9]\+/XR_MGMT_INTERFACES: linux:eth0/g' ~/XRd-Labs/clus25-devwks3337/docker-compose.yml
```

We also need to update the network interface to point to macvlan.

```bash
sed -i 's/xrd-[0-9]\+-mg0: null/macvlan0: null/g' ~/XRd-Labs/clus25-devwks3337/docker-compose.yml
```

### Start XRd Instances - 198.18.134.28

```bash
docker-compose -f ~/XRd-Labs/clus25-devwks3337/docker-compose.yml up -d
```

### Verification - 198.18.134.28

After finishing all the steps above, you should have a working XRd topology. To verify:

1. On `198.18.134.28`, check that all containers are running:

```bash
docker ps
```

2. Review how XRd is booting up.

```bash
docker logs -f xrd-1
```

Once you ISIS come up, XRd should be ready to take SSH connections.

> [!NOTE]  
> You can watch all XRd logs at once by using `docker compose logs -f` make sure you are on the directory that has the compose file.

## Configure gNMI on XRd Instances - 192.18.134.29

On the `192.18.134.29` VM configure gNMI on the XRd devices using ansible:

```bash
cd /root
git clone https://github.com/jillesca/DEVWKS-3337
```

```bash
cd /root/DEVWKS-3337/ansible/ \
&& ansible-playbook xrd_apply_config.yaml
```

> [!TIP]
> This playbook enables gNMI on all XRd devices so they can communicate with our agents.

### Test gNMI configuration - Workshop Laptop

On the workshop laptop, verify the gNMI configuration is working on the XRd containers.

```bash
cd /home/devnet/DEVWKS-3337/gNMIBuddy/ \
&& uv run cli_app.py --inventory xrd_inventory.json  --device xrd-1 mpls --detail \
cd -
```

## Next Steps

Continue now to [Setup Langgraph](SETUP_LANGGRAPH.md) to configure the AI agents that will interact with your network.

TODO:

- Add how to enter the XRd cli from the container itself.
  - Using bash and docker attatch
