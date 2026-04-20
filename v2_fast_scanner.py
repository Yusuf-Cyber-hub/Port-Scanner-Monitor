import socket
import time
import concurrent.futures

target = "X.X.X.X" # IP dyal PC dyalk (Localhost)
print(f"[*] Starting FAST Scan (Multithreaded) on {target}...")

start_time = time.time()

# Function li kat-scanni port wa7ed
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()

# Hna kankhldmo b 100 Threads (100 khedam kayscanniw f nefs l-weqt)
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1, 1025):
        executor.submit(scan_port, port)

end_time = time.time()
print(f"[*] Scan finished in {end_time - start_time:.2f} seconds.")