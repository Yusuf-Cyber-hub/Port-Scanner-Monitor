# 🛡️ Stateful Port Monitor (Blue Team IDS Concept)

## 📌 Project Overview
This project demonstrates the evolution of a Python-based Network Scanner. It transitions from a basic sequential port scanner into an **Automated Stateful Port Monitor**, designed with **Blue Team (Defensive Security)** principles in mind. 
It scans a target IP, saves the open ports as a baseline, and alerts the administrator if unauthorized ports are opened or closed in future scans.

## 🚀 The Evolution (3 Versions)
This project is divided into three stages to demonstrate continuous improvement and performance optimization:

* **[V1] Basic Scanner (`v1_basic_scanner.py`):** A standard, single-threaded port scanner. It is slow as it scans ports sequentially.
* **[V2] Fast Scanner (`v2_fast_scanner.py`):** Implements `concurrent.futures.ThreadPoolExecutor` for Multithreading, making the scan exponentially faster.
* **[V3] Stateful Monitor (`v3_stateful_monitor.py`):** The final Blue Team tool. It introduces CLI arguments (`argparse`), saves scan history locally in a JSON file, and performs logical comparisons to detect network changes.

## 🛠️ Features of V3 (The Monitor)
- **Fast Execution:** Uses 100 concurrent threads.
- **Stateful Baseline Tracking:** Saves previous scan results in `scan_history.json`.
- **Intrusion Detection (IDS Logic):** Alerts on **Newly Opened Ports** 🚨 and **Closed Ports** ⚠️.
- **Multi-Target Support:** The JSON history uses a dictionary structure. You can scan multiple different IPs (e.g., a web server and a database server), and the tool will track each IP's history independently without overwriting the others!
- **Data Privacy:** Uses `.gitignore` to prevent leaking local scan histories to public repositories.

## 💻 How to Use (V3)
1. Clone the repository:
   ```bash
   git clone https://github.com/Yusuf-Cyber-hub/Port-Scanner-Monitor.git
2. Navigate to the directory:
     ```bash
        cd Port-Scanner-Monitor
3. Run the Stateful Monitor via CLI:
    ```bash
        python v3_stateful_monitor.py -i x.x.x.x

## ⚠️ Security Disclaimer :
- This tool is created for Educational Purposes and internal network monitoring only. Do not use this tool to scan networks or IP addresses that you do not own or have explicit permission to scan.