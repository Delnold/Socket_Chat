import socket
import threading

host = '192.168.1.39' # Your local IP-Adress  (cmd > ipconfig to find out yours)
port = 9090
array_of_clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(6)


def new_client(server):
    conn, adress = server.accept()
    array_of_clients.append(conn)
    return conn, adress


def handling_messages(server):
    conn, adress = new_client(server)
    conn.send(f"User{adress}".encode("utf-8"))
    while True:
        data = conn.recv(10240).decode("utf-8")
        print(data)
        for i in array_of_clients:
            if i != conn:
                i.send(data.encode("utf-8"))
            else:
                continue

while True:
    threading.Thread(target=handling_messages, args=(server,)).start()




