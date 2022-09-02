
import socket

PORT = 5050
HEADER = 60
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'Disconnected !!!'
SERVER = socket.gethostbyname(socket.gethostname())
Address = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(Address)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    

send("Hello server socket. Client socket here.")
input()
send("Let's make a connection by applying the fundamentals of networking and socket.")
input()
send("Bye!!!")
input()
send(DISCONNECT_MESSAGE)







