import socket
import concurrent.futures # La librairie jdida dyal ssor3a (Multithreading)
from datetime import datetime

# L'IP li bghiti t-scanni
target = "X.X.X.X"

print("-" * 50)
print(f"Bdit l-scan mjehed dyal l'IP : {target}")
print(f"Lwe9t : {str(datetime.now())}")
print("-" * 50)

# Fonction kat-scanni port wa7d
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] L-Port {port} m7loul (Open) !")
            
        s.close()
    except:
        pass # Ila w9e3 mochkil, matdir walo kml

# Hna fin kayn ssir dyal ssor3a
# max_workers=100 kat3ni 100 port kayt-scannaw f d9a we7da
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Ghan-scanniw mn port 1 tal port 1024
    for port in range(1, 1025):
        executor.submit(scan_port, port)

print("-" * 50)
print("L-Scan V2 sala f ramchat 3in !")