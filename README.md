# Network Automation Simulator

This project simulates a basic network automation pipeline using Python. It mimics connecting to Cisco IOS network devices via SSH, executing configuration and monitoring commands, parsing VLAN outputs, and logging network states—all **without requiring access to real hardware**.

Designed to demonstrate your understanding of automated network workflows and scripting logic, this project is ideal for **network engineering internship portfolios**.

---

## 🚀 Features

- Simulated SSH-based device connection with error handling
- Simulated command execution (`show vlan brief`, etc.)
- VLAN output parsing with structured data extraction
- Centralized logging with timestamped session tracking
- Designed to be run on any local machine (no hardware required)

---

## 🧰 Tech Stack

- **Python 3.10+**
- `datetime`, `os` – Standard libraries
- Designed for CLI environments (Windows, macOS, Linux)

---

## 📁 Project Structure

```bash
network-automation-simulator/
├── main.py              # Main simulation script
├── vlan_parser.py       # Parses VLAN output (simulated)
├── device_simulator.py  # Contains device info and mock SSH logic
├── utils.py             # Helper functions and logging
├── sample_vlans/        # Directory with sample "show vlan brief" outputs
└── logs/                # Auto-created folder with timestamped logs
```

## 🔧 Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/yourusername/network-automation-simulator.git
cd network-automation-simulator

# 2. (Optional) Create a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# 3. Run the Simulation (no external dependencies required)
python main.py
```
