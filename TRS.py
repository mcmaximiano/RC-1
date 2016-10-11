def word_translate(lang_file, word):
	lang_file.seek(0) # restart read pointer to beginning
	for line in lang_file.readlines():
		(estrg, tuga) = line.split()
		if tuga == word:
			return estrg
	return None # if no such image is avaliable
		
def image_translate(img_file, filename):
	'''
	Returns the filename corresponding to the translation image.
	Returns None if no such translation exists.
	'''
	img_file.seek(0) # restart read pointer to beginning
	for line in img_file.readlines():
		(estrgf, tugaf) = line.split(' ', 1)
		if tugaf == filename:
			return estrgf
	return None # if no such image is avaliable

def recv1(acceptable):
		'''
		acceptable: 'bytes'-type containing the acceptable characters to be
		received in the socket.
		Returns the read byte if it's in acceptable.
		Otherwise it raises ValueError.
		'''
		byte = conn_sock.recv(1)
		if byte in acceptable:
			return byte
		else:
			raise SyntaxError('Received byte from client was unexpected.')

def recvTRQ():
	msg = ''
	for byte in b'TRQ ':
		msg += recv1(byte)
	msg += recv1(b' ')
	msg += recv1(b'tf')
	if msg.endswith(b't'):
		msg += recvTRQtext()
	elif msg.endswith(b'f'):
		msg += recvTRQfile()
	return msg

def recv_word():
	word = b''
	while not word.endswith(b' '):
		word += conn_sock.recv(1)
	return word

def recvTRQfile():
	msg  = recv1(' ')
	msg  += recv_word() # recv filename
	size = recv_word() 	# recv file size
	msg  += size
	size = int(size)
	msg  = recv1(' ')
	msg  += recv(size)	# recv file content
	msg  = recv1(' ')
	return msg	
			
def recvTRQtext():
	msg = recv1(' ')
	N = recv_word() # if we don't receive an int-able, int() raises ValueError
	msg += N
	N = int(N)
	msg = recv1(' ')
	while N > 0:
	

def sendTRS_ERR():

def sendTRS(conn_sock):

def sendTRS_ERR(conn_sock):

def sendTRS_NTA(conn_sock):
