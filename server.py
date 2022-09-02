import socket
import threading


HEADER = 60
FORMAT = 'utf-8' # KIND OF BYTES.
PORT = 5050
DISCONNECT_MESSAGE = 'Disconnected !!!'
SERVER = socket.gethostbyname(socket.gethostname())
#print(socket.gethostname())
#print(SERVER)



Address = (SERVER,PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Address)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} is connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
          msg_length = int(msg_length)
          msg = conn.recv(msg_length).decode(FORMAT)

          if msg == DISCONNECT_MESSAGE:
               connected = False

        print(f"[{addr}] {msg}")
        conn.send("[MESSAGE] is recieved".encode(FORMAT))
    conn.close()


        

def start():
    server.listen()
    print(f"[SERVER] server is listening on {SERVER}")
    while True:
        (conn,addr) =  server.accept()
        thread = threading.Thread(target = handle_client, args = (conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    

print("[SERVER] server is starting !!!")
start()

