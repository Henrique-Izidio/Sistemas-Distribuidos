import socket
from datetime import datetime

host = "127.0.0.1"
port = 8000

serverAddress = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(5.0)

message = "Hora Atual"

sock.connect(serverAddress)

while True:
    try:

        data = sock.recv(1024)
        print(f"{data.decode('UTF-8')}")

        message = input()
        sock.sendall(message.encode('UTF-8'))

    except socket.timeout:
        print("Conexão Encerrada")
        break
