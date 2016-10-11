from socket import *

# enum

class nlsocket(socket):
	'''
	Subclass of socket.socket. Two sole differences:
	- nlsockets offer 'nl' functions that do multiple recvs/sends until a 
	newline is read/written.
	'''
	recv_size = 512

	def __init__(self, address_family, socket_type):
		super().__init__(address_family, socket_type)

	def nlrecv(self):
		'''
		Does multiple recvs until it finds a newline.
		'''	
		msg = b''
		while not msg.endswith(b'\n'):
			msg += self.recv(self.recv_size)
		return msg
		
	def nlrecvfrom(self):
		'''
		Same as normal recvfrom, but only stops reading when it finds a newline.
		Does not take a 'buffersize' argument since it only stops at the newline.
		'''
		(msg, addr) = self.recvfrom(self.recv_size)
		while not msg.endswith(b'\n'):
			msg += self.recv(self.recv_size)
		return (msg, addr)

	def nlsend(self, msg):
		if not msg.endswith(b'\n'):
			msg += b'\n'
		sentc = 0
		while sentc < len(msg):
			sentc += self.send(msg[sentc:])
		return sentc

	def nlsendto(self, msg, addr):
		if not msg.endswith(b'\n'):
			msg += b'\n'
		sentc = 0
		while sentc < len(msg):
			sentc += self.sendto(msg[sentc:], addr)
