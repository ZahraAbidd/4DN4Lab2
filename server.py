import socket

# AF_INET is IPV4 and SOCK_STREAM implies TCP connection 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 1234 is just a random local port
s.bind((socket.gethostname(), 1234)) 

# 5 is the queue size
s.listen(5)

while True:
    # clientsocket = socket object, and the address is where the incoming packet is coming from
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    clientsocket.send(bytes("welcome to server", "utf-8"))
