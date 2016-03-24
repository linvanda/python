import socket

for i in range(20, 25):
	try:
		s = socket.socket()
		s.connect(('127.0.0.1', i))
	
		s.send('H')

		banner = s.recv(1024)
		if banner:
			print "port" + str(i) + "open"
		s.close()
	except:pass

