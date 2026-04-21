import socket
import time

# Target IP (Change x.x.x.x to the IP you want to scan)
TARGET_IP = "x.x.x.x" 

print(f"[*] Starting Basic Sequential Scan on {TARGET_IP}...")

start_time = time.time()

# Scanning ports from 1 to 1024 (Well-known ports)
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1) 
    
    # connect_ex returns 0 if the connection was successful (Port is OPEN)
    result = s.connect_ex((TARGET_IP, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
        
    s.close()

end_time = time.time()
print(f"[*] Scan finished in {end_time - start_time:.2f} seconds.")