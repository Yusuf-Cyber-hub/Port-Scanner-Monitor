import socket
import time
import concurrent.futures

TARGET_IP = "x.x.x.x"  # Change to the IP you want to scan
print(f"[*] Starting FAST Multithreaded Scan on {TARGET_IP}...")

start_time = time.time()

def scan_port(port):
    """Attempts to connect to a specific port to check if it's open."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((TARGET_IP, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()

# Using ThreadPoolExecutor to run multiple port scans concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1, 1025):
        executor.submit(scan_port, port)

end_time = time.time()
print(f"[*] Scan finished in {end_time - start_time:.2f} seconds.")