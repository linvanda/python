import socket

addr = ('localhost', 1024)
buf_size = 128

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	data = raw_input('pls enter string:')
	if not data :
		break
	udp_client.sendto(data, addr)
udp_client.close()
