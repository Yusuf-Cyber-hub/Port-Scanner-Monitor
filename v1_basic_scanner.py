import socket
import time

target = "X.X.X.X" # IP dyal PC dyalk (Localhost)
print(f"[*] Starting BASIC Scan on {target}...")

start_time = time.time()

# Ghadi n-scanniw mn port 1 hta l 1024 (Les ports l-mohimin)
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1) # Kantsnaw 0.1s f kola port
    
    # connect_ex katrj3 0 ila kan l-port m7loul
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
        
    s.close()

end_time = time.time()
print(f"[*] Scan finished in {end_time - start_time:.2f} seconds.")