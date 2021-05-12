#0. import socket module
import socket

target_host = "127.0.0.1"   # insert ip addr of target
target_port = 80            # insert port. Port 80 commonly used in Hypertext Transfer Protocol(http)

#1. create a socket object                                    # AF_INET = address family of IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # SOCK_DGRAM = call on a datagram-based protocol. You send one datagram and get one reply and then the connection terminates.

#2. send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))   #sending a byte-string data **Python 3

#3. receive some data
data, addr = client.recvfrom(4096) 

print (data)    # ***having some errors printing data received.

'''
NOTE: Traceback (most recent call last):
  File "/home/user/Documents/Projects/black-hat-python/2-The Network: Basics/2.2-udp-client.py", line 11, in <module>
    client.sendto("AAABBBCCC",(target_host,target_port))
TypeError: a bytes-like object is required, not 'str'

Again, remember that Python 3.X takes a bytes parameter. 
Thus you have to define the data to be sent as a byte-string or call on the 'encode' method, str.encode().
Alternatively, adding 'b' before the string data will work. eg) ..(b"this is a string data")
This works for Python 2.X as well.


NOTE: How to check if this code works?

1) Open 2 terminal tab. (I am using Kali Linux 2021.1)

2) Tab 1 - Key in: nc -nvulp [insert listener port, eg) 80]         
# nc = netcat, -n = numeric-only IP addresses, no DNS, -v = verbose [use twice to be more verbose], -u = UDP mode, 
# -l = listen mode, for inbound connects, -p = local port number (port numbers can be individual or ranges: lo-hi [inclusive])

3) Tab 2 - Run the python udp-client code, eg) python3 udp-client.py

4) Tab 1 - See the output. 

nc -nvulp 80                                                                                                            148 ⨯ 1 ⚙
listening on [any] 80 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 43539
AAABBBCCC

^Z to stop listening.

'''