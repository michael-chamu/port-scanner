import socket


def scan (host, start_port, end_port):
    print(f"Scanning {host}.......")
    for port in range(start_port, end_port +1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex(host, port)
            if result == 0:
                print(f" Port {port}: OPEN")
            s.close()
        except Exception as e:
            pass

scan("scanme.nmap.org", 20, 100)