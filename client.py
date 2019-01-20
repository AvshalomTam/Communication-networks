import sys
from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
msg = raw_input()
while not msg == 'quit':
    s.sendto(msg, (sys.argv[1], int(sys.argv[2])))
    data, sender_info = s.recvfrom(2048)
    print data
    msg = raw_input()
s.close()
