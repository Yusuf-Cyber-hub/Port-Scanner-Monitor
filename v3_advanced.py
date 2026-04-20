import socket
import concurrent.futures
import json
import os
import argparse

# 1. Configuration dyal Argparse (Bach nakhdo IP mn Terminal)
parser = argparse.ArgumentParser(description="Stateful Port Monitor - Blue Team IDS")
parser.add_argument("-i", "--ip", required=True, help="Target IP address to monitor (e.g., 127.0.0.1)")
args = parser.parse_args()

target_ip = args.ip
history_file = "scan_history.json" # L-fichier fin ghadi n-saviw l-historique
open_ports = [] # Hna ghadi njm3o l-ports li lqina lyouma

print(f"[*] Starting Stateful Monitor on IP: {target_ip}...")

# 2. La fonction d Scan (bhal V2)
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        open_ports.append(port) # Ila lqinah m7loul, kanzidouh f la liste
    s.close()

# Kankhdmo b 100 Threads bach nzrbo 
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1, 1025):
        executor.submit(scan_port, port)

# Kanrtbou l-ports sghar homa lwlin (facultatif mais katban nqiya)
open_ports.sort()

# ==========================================
# 3. LOGIQUE DYAL BLUE TEAM (Comparaison IDS)
# ==========================================

old_ports = []

# Kan9lebo wach l-fichier JSON kayn (wach fayt lina derna scan mn qbel?)
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        data = json.load(file)
        # Kanjbdo l-ports l-qdam dyal had l-IP (ila kano)
        old_ports = data.get(target_ip, [])

# Hna l-Qaleb: Kanqarno l-Qdim m3a Jdid (Kankhdmo b 'Sets' f Python)
# Set kat3tina l-farq bin jooj d les listes bzarba
newly_opened = list(set(open_ports) - set(old_ports))
newly_closed = list(set(old_ports) - set(open_ports))

print("\n--- [ MONITORING RESULTS ] ---")

if not old_ports:
    # Ila makanch historique, kan3lmo l-user bli hada awel scan
    print("[i] First time scanning this IP. Saving baseline...")
    print(f"[+] Currently Open Ports: {open_ports}")
else:
    # Ila kan l-historique, kan3tiw les ALERTES
    if newly_opened:
        print(f"🚨 [ALERTE] NEW PORTS OPENED: {newly_opened} (Possible Breach!)")
    if newly_closed:
        print(f"⚠️ [INFO] PORTS CLOSED: {newly_closed} (Service stopped)")
    
    if not newly_opened and not newly_closed:
        print("[V] Network is SECURE. No changes detected.")

# F lkher, kan-sauvegardiw l-Scan d lyouma bach ykon houa l-reference d gheda
data_to_save = {}
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        data_to_save = json.load(file)

data_to_save[target_ip] = open_ports

with open(history_file, "w") as file:
    json.dump(data_to_save, file, indent=4) # Indent=4 katkhali l-fichier JSON mktoub mzyan

print("------------------------------")