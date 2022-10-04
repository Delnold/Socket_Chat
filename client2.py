import socket
import threading

host = '192.168.1.39' # Your local IP-Adress  (cmd > ipconfig to find out yours)
port = 9090

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect((host, port))
print(ClientSocket.recv(10240).decode("utf-8"))


def Send_Messages():
    text = input()
    return ClientSocket.send(text.encode("utf-8"))


def Receiving_Messages():
    print(ClientSocket.recv(10240).decode("utf-8"))


while True:
    threading.Thread(target=Send_Messages).start()
    threading.Thread(target=Receiving_Messages).start()
