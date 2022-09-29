# Socket Programming in Pytho

Using socket programming, two nodes on a network can connect and communicate with one another. The other socket (node) reaches out to the first socket to establish a connection while the first socket listens on a certain port at an IP. While the client reaches out to the server, the server creates the listener socket.

Importing the socket library and creating a basic socket are the first steps in socket programming.

# A simple server-client program : 

Here, two parameters were supplied to a socket instance that was created. AF INET is the first parameter, while SOCK STREAM is the second. AF_INET stands for ipv4 address-family. The connection-oriented TCP protocol is referred to as SOCK_STREAM.
Now that we have this socket, we can connect to a server.

## Server:

A server's bind() method ties it to a particular IP address and port so it can listen for incoming requests on those addresses and ports. A server's listen() method activates listening mode on the server. As a result, the server is able to monitor incoming connections. Finally, a server has the methods accept() and close(). A connection with the client is established by the accept method, and it is cut off by the close method.

### SERVER CODE (Explanation)=> 

1. server = socket.socket() --> By using the specified address family, socket type, and protocol number, it merely establishes a new socket. 
2. PORT = 5050 --> Reserves a port for computer
3. Address = (SERVER,PORT), server.bind(Address) --> Our server was bound to the designated port. It would have only listened to calls made on the local machine if we had passed 127.0.0.1.
4. server.listen() --> Server can connect to clients. 
5. server.close() --> Closes the socket, making any subsequent operations on it unsuccessful.

## Client: 
At this point, we need something that a server can communicate with. To confirm that our server is operational, we might connect to it in this way.

### CLIENT CODE (Explanation)=> 
1. We create a socket object first.
2. Next, we establish a connection to localhost on the port used by our server, after which we request data from the server and then cut off the connection.
3. After launching the server script, save this file as client.py and run it from the terminal.

## References 

 - [Python Socket Network Programming](https://yasoob.me/2013/08/06/python-socket-network-programming/)
 - [NETWORK PROGRAMMING - SERVER & CLIENT : BASICS](https://www.bogotobogo.com/python/python_network_programming_server_client.php)
 - [socket — Low-level networking interface (Python Doc.)](https://docs.python.org/3/library/socket.html)

## Tech Stack

**Client:** Python, Socket Library

**Server:** Python, Socket Library


## Author
- Sitam Meur
 [sitammeur@gmail.com], 
 Feel free to mail me for any queries. 

## Contributions 
  
  Issues and Pull requests are most welcome. 
