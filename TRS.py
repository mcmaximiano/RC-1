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

def recvULQ():
	return recv_word(3, b'ULQ')

def recvULR():
	pass

def recvUNQ():
	unq = recv_word(3, b'UNQ')
	unq = recv_word(MAX_LANG_LEN)
	return unq

def recvUNR():
	unr  = recv_word(3, b'UNR')
	unr += recv_word(MAX_IP_LEN)	# get IP/hostname
	unr += recv_word(MAX_PORT_LEN) 	# get port
	return unr

def recvTRQ():
	trq  = recv_word(3, b'TRQ')
	sub  = recv1(b'tf')
	msg += sub
	if sub == b't':
		msg += recvTRQtext()
	elif sub == b'f':
		msg += recvTRQfile()
	return msg

	def recvTRQfile():
		msg  = recv1(b' ')
		msg  += recv_word() 	# recv filename
		size = recv_word() 		# recv file size
		msg  += size
		msg  = recv1(b' ')
		msg  += recv(int(size))	# recv file content
		msg  = recv1(b' ')
		return msg	
			
	def recvTRQtext():
		msg = recv1(b' ')
		N = recv_word()
		msg += N
		msg = recv1(b' ')
		for _ in range(int(N)):
			msg += recv_word()	
		return msg

def recvTRR():
	msg  = recv_word(3, b'TRR')
	msg += recv1(b' ')
	msg += recv1(b'tf')
	if msg.endswith(b't'):
		msg += recvTRQtext()
	elif msg.endswith(b'f'):
		msg += recvTRQfile()
	return msg

	def recvTRRfile():
		msg  = recv1(b' ')
		msg  += recv_word() 	# recv filename
		size = recv_word() 		# recv file size
		msg  += size
		msg  = recv1(b' ')
		msg  += recv(int(size))	# recv file content
		msg  = recv1(b' ')
		return msg	
				
	def recvTRRtext():
		msg = recv1(b' ')
		N = recv_word()
		msg += N
		msg = recv1(b' ')
		for _ in range(int(N)):
			msg += recv_word()	
		return msg

		
def recvSRG():
	srg =  recv_word(3, b'SUN')
	srg += recv_word(MAX_LANG_LEN) 	# recv language
	srg += recv_word(MAX_IP_LEN)	# recv IPTRS
	srg += recv_word(MAX_PORT_LEN) 	# recv portTRS
	return srg # XXX check for correctness
	
def recvSRR():

	

def recvSUN():
	sun =  recv_word(3, b'SUN')
	sun += recv_word(MAX_LANG_LEN) 	# recv language
	sun += recv_word(MAX_IP_LEN)	# recv IPTRS
	sun += recv_word(MAX_PORT_LEN) 	# recv portTRS
	return sun # XXX check for correctness

def recvSUR():








def sendTRS_ERR():

def sendTRS(conn_sock):

def sendTRS_ERR(conn_sock):

def sendTRS_NTA(conn_sock):
