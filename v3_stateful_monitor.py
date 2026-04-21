import socket
import concurrent.futures
import json
import os
import argparse

# 1. CLI Argument Parsing
parser = argparse.ArgumentParser(description="Stateful Port Monitor - Blue Team IDS")
parser.add_argument("-i", "--ip", required=True, help="Target IP address to monitor")
args = parser.parse_args()

target_ip = args.ip
history_file = "scan_history.json"
open_ports = [] 

print(f"[*] Starting Stateful Monitor on IP: {target_ip}...")

# 2. Fast Multithreaded Scan Function
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        open_ports.append(port)
    s.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1, 1025):
        executor.submit(scan_port, port)

open_ports.sort()

# ==========================================
# 3. BLUE TEAM LOGIC: Stateful Comparison
# ==========================================

old_ports = []

# Load previous scan history if it exists
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        data = json.load(file)
        old_ports = data.get(target_ip, [])

# Compare sets to find differences
newly_opened = list(set(open_ports) - set(old_ports))
newly_closed = list(set(old_ports) - set(open_ports))

print("\n--- [ MONITORING RESULTS ] ---")

if not old_ports:
    print("[i] First time scanning this IP. Saving baseline...")
    print(f"[+] Currently Open Ports: {open_ports}")
else:
    if newly_opened:
        print(f"🚨 [ALERT] NEW PORTS OPENED: {newly_opened} (Possible Breach!)")
    if newly_closed:
        print(f"⚠️ [INFO] PORTS CLOSED: {newly_closed} (Service stopped)")
    
    if not newly_opened and not newly_closed:
        print("[V] Network is SECURE. No changes detected.")

# Save the current scan as the new baseline
data_to_save = {}
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        data_to_save = json.load(file)

data_to_save[target_ip] = open_ports

with open(history_file, "w") as file:
    json.dump(data_to_save, file, indent=4)

print("------------------------------")