from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
source_ip = '127.0.0.1'
source_port = 8080
s.bind((source_ip, source_port))
while True:
	data, sender_info = s.recvfrom(2048)
	print "Message: ", data, " from: ", sender_info
	s.sendto(data.upper(), sender_info)