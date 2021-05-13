#0. import modules
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port)) 

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#1. this is our client-handling thread
def handle_client(client_socket): 

    #2. print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    #3. send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while True:

    client,addr = server.accept() 
    
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
 
    #4. spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start() 


"""

**NOTE: Code able to function in Python 2.X

**NOTE: Running in Python 3 Error

File "/home/user/Documents/Projects/black-hat-python/2-The Network: Basics/2.3-tcp-server.py", line 13
    print "[*] Listening on %s:%d" % (bind_ip,bind_port)

"""