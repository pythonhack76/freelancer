import socket

HOST = "127.0.0.1"  #IP address or server's hostname
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello Hackers")
    data = s.recv(1024)

print(f"Ricevuto {data!r}")
