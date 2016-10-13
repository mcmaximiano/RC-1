class ProtocolError(Exception): pass

def parseULQ(ulq):
	return ulq == b'ULQ\n'
	
def parseULR(ulr):
	'''
	Returns all avaliable languages in a list.
	'''
	sp = ulr.split(b' ')
	langc = sp[0:1]
	langs = sp[1:]
	#TODO maybe: check each individual word for length
	return sp[0] == b'ULR' and ulr.endswith(b'\n') and
		langc.isdigit() and int(langc) == len(langs) 

def parseUNQ(unq):
	'''
	Returns the requested language.
	'''
	sp = unq.split(b' ')
	if sp[0] == b'UNQ' and len(sp) == 2  and ulr.endswith(b'\n'):
		return sp[1].encode()
	else:
		return None
	
def parseUNR(unr):
	'''
	Returns the requested TRS in (addr, port) form.
	'''
	sp = unr.split(b' ')
	if sp[0] == b'UNR' and len(sp) == 3 and ulr.endswith(b'\n')
	and sp[2].isdigit():
		return (sp[1].decode(), int(sp[2]))
	else:
		return None

def parseTRQ(trq):
	'''TRQ is passed by TCP so has to be read byte-by-byte'''
	return NotImplemented

def parseTRR(trr):
	'''TRR is passed by TCP so has to be read byte-by-byte'''
	return NotImplemented

def parseSRG(srg):
	'''Returns the new TRS in {language: (addr, port)} form'''
	sp = unq.split(b' ')
	if len(sp) == 4 and sp[0] == b'SRG' and srg.endswith(b'\n')
	and sp[3].isdigit():
		return {sp[1].decode(): (sp[2].decode(), sp[3])}

def parseSRR():
	sp = unq.split(b' ')
	if len(sp) == 2 and sp[0] == b'SRR' and 
	(sp[1] == b'ERR' or sp[1] == b'OK' or sp[1] == b'ERR') and
	srg.endswith(b'\n'):
		return sp[1].decode()
	
def parseSUN():
	return NotImplemented #TODO

def parseSUR():
	return NotImplemented #TODO

def recv_word(maxlen):
	word = b''
	while not word.endswith(b' ') or word.endswith('\n'): #XXX hack
		char = conn_sock.recv(1)
		if char in string.letters + string.digits and len(word) <= maxlen + 1:
			word += char
		else:
			raise ValueError
	return word

def recvTRQ(socket):
	if recv_word(3) == b'TRQ':
		2nd = recv_word(3)
		if 2nd == 't':
			return recvTRQtext()
		if 2nd == 'f':
			return recvTRQfile()
		if 2nd == 'ERR':
			return 'ERR'
		if 2nd == 'NTA':
			return 'NTA'
	else:
		return None

	def recvTRQfile():
		filename = recv_word(100)
		size     = recv_word(10)
		if not size.isidigit(): return None
		content  = recv(int(size))
		return (filename.decode(), int(size), content)
				
	def recvTRQtext():
		langs = []
		N = recv_word(3)
		if not N.isidigit():
			return None
		for _ in range(int(N)):
			langs.append(recv_word(LANG_LEN))
		if not recv(1) == b'\n':
			return None
		return langs

def recvTRR(socket):
	if recv_word(3) == b'TRR':
		2nd = recv_word(3)
		if 2nd == 't':
			return recvTRRtext()
		if 2nd == 'f':
			return recvTRRfile()
		if 2nd == 'ERR':
			return 'ERR'
		if 2nd == 'NTA':
			return 'NTA'
	else:
		return None

	def recvTRRfile():
		filename = recv_word(100)
		size     = recv_word(10)
		if not size.isidigit(): return None
		content  = recv(int(size))
		return (filename.decode(), int(size), content)
				
	def recvTRRtext():
		words = []
		N = recv_word(3)
		if not N.isidigit():
			return None
		for _ in range(int(N)):
			words.append(recv_word(LANG_LEN))
		if not recv(1) == b'\n':
			return None
		return words

