# 0. import socket module
import socket

target_host = "www.google.com"     # insert website "[]"
target_port = 80                   # port 80 commonly used in Hypertext Transfer Protocol(http)

# 1. create a socket object                                 # socket instance with 2 parameters(AF_INET & SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = address family of IPv4   # SOCK_STREAM = connection oriented TCP protocol
                                                            
# 2. connect the client
client.connect((target_host,target_port))                   # client calls connect() to establish connection to the server & initiate 3-way handshake

# 3. send some data                                     
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"   # data = string 
client.send(data.encode('utf-8'))                     # refer below for further explanation on 'encode'

# 4. receive some data (up to 4096 bytes)
response = client.recv(4096).decode('utf-8')          # refer below for further explanation on 'decode'

print(response)                                       # print received 'response' set in #4


'''

#3. sending data

If Python 2.X is used, code may look as such:
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data)
There is no need for the additional call for 'encoding' in Python 2.X.
As in the documentation for python2, socket.send() takes a string parameter.

However, if Python 3.X is used:
socket.send() in Python 3.X takes a bytes parameter. 
Thus you have to convert your string data into bytes using str.encode().
Alternatively, adding 'b' in  data = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n" will change the 'string' into a 'byte-string'.
There is no need to call for 'encode' if this method is used.

#4. receiving data
Similar to above explanation.
The use of .decode is needed to convert the byte-data to string-data.

**Note: 
TCP/IP is a stream-based protocol, not a message-based protocol. 
There's no guarantee that every send() call by one peer results in a single recv() call by the other peer receiving the exact data sent.
Data might be received in pieces, split across multiple recv() calls, due to packet fragmentation.
Therefor,receiving up to 4096 byte = 4 KiB or a 512 to 4096 byte range would be recommended.

'''