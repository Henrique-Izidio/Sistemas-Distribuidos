from socket import *
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8000

def clientConnection(con, address):

    options = """
========================================
... [Opções do Menu] ...
========================================
1. Ver horário
2. Inverter String
3. Fechar Conexão
"""

    while(True):

        con.sendall(options.encode('utf-8'))

        data = con.recv(1024)

        if data.decode() == "1":
            con.sendall(getTime())
        elif data.decode() == "2":
            con.sendall(reverseStr(con))
        elif data.decode() == "3":
            closeCon(con)
            break
        else:
            message = "Opção invalida"
            con.sendall(message.encode('UTF-8'))

def getTime():
    timeStr = datetime.now().strftime("%H:%M:%S")
    timeBytes = timeStr.encode('UTF-8')
    return timeBytes

def reverseStr(con):
    message = "Qual String deve ser invertida?"
    con.sendall(message.encode('UTF-8'))
    
    data = con.recv(1024)

    print(data.decode('UTF-8'))

    reverse = "".join(reversed(data.decode('UTF-8')))
    
    return reverse.encode('UTF-8')

def closeCon(con):
    message = "Encerrando Conexão..."
    con.sendall(message.encode('UTF-8'))

    return message



def initServer():
    threadManager = ThreadPoolExecutor(max_workers=10)

    serverSock = socket(AF_INET, SOCK_STREAM)

    serverSock.bind((HOST, PORT))

    serverSock.listen()

    while True:
        con, address = serverSock.accept()
        threadManager.submit(clientConnection, con, address)


if __name__ == "__main__":
    initServer()