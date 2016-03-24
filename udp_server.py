import socket

host = ''
port = 1024
buf_size = 128
addr = (host, port)

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(addr)

while True:
	print 'waiting for message...'
	data, addr = udp_server.recvfrom(buf_size)
	print '---received from and return to:' + str(addr) + ': ' + data

udp_server.close()
