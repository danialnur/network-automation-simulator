# Network Automation Simulator

A small Python project exploring automated network device configuration with [Netmiko](https://github.com/ktbyers/netmiko), built without needing access to real switches or routers.

It's two pieces, not fully wired together yet:

- **`main.py`** — a simulated demo runner. For each device in a hardcoded list, it logs a timestamped, fake SSH session (`show vlan brief` output) without opening a real connection.
- **`netmiko_handler.py`** — a real Netmiko helper (`send_config`) that connects to an actual Cisco IOS device over SSH and pushes commands from a file. Not currently called from `main.py`.
- **`device_inventory.csv`** / **`config_commands.txt`** — sample inventory and config-push formats the two pieces above are built around.

## Setup

```bash
git clone https://github.com/danialnur/network-automation-simulator.git
cd network-automation-simulator
pip install -r requirements.txt
python main.py
```

`main.py` runs standalone with no network access required — it only prints the simulated session. To push config to a real device with `netmiko_handler.py`, call `send_config()` with a device dict (matching the columns in `device_inventory.csv`) and a path to a command file (see `config_commands.txt`).

## Next step

Wire `main.py`'s `simulate = False` branch to call `netmiko_handler.send_config()` for each device in `device_inventory.csv`, so the demo path and the real path run the same code.
