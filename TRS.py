def get_word_trans(lang_file, word):
	lang_file.seek(0) # restart read pointer to beginning
	for line in lang_file.readlines():
		(estrg, tuga) = line.split()
		if tuga == word:
			return estrg
	return None # if no such image is avaliable

		
def get_image_trans_filename(img_file, filename):
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


def sendTRRtext(msg, listener):
	'''
	Responds to TRQ t ...
	'''
	msg_len = str(len(msg)-1
	answer = 'TRR ' + msg[0] + ' ' + msg_len
	for el in msg[1:]
		answer += ' ' +  get_word_trans('text_translation.txt', el)
	print('Sending:\n' + answer_msg + '\n...to:', listener)
	return answer

                       
def sendTRRfile(msg, listener):
	'''
	Responds to TRQ f ...
	'''
	filename = msg[1]
	trans_file_name = get_image_trans_filename('file_translation.txt', filename)
	answer_file = open(trans_file_name, 'rb')
	data = file.read()
	size = len(conteudo)
	answer = 'TRR ' + msg[0] + ' ' + trans_file_name + ' ' + bytes[size] + ' ' + data 
	print('Sending file:\n' + trans_file_name + '\n...to:', listener)
	return answer


def TRSloop(listener):
	while 1:
		(server, clientaddr) = listener.accept()
		msg = recvTRQ(listener)
			if (msg[0] == t):
				answer = sendTRRtext(msg, listener)
				answer.encode()
				self.sock.nlsendto(answer, listener)
				print('Message sent!')
			elif (msg[0] == f):
				answer = sendTRRfile(msg, listener)
				answer = answer.encode()
				self.sock.nlsendto(answer, listener)
				print('File sent!')
			else return 'TRQ ERR'


def sendSRG(lang, nameTRS, port):
	msg = 'SRG ' + ' ' + lang + ' ' + nameTRS + ' ' + port
	sock.nlsendto(msg, (TCSip, TCSport))
	print('SRG Msg sent!')
	return msg

def recvSRR():
	if sock.recv(4) == b'SRR ':
		2nd = sock.recv(2)
		if 2nd == 'OK':
			status = 'OK'
			return status
		elif 2nd == 'NO':
			status = 'NOK'
			return status
		else:
			status = 'SRR ERR'
			return status

def sendSUN():
	msg = 'SUN ' + ' ' + lang + ' ' + nameTRS + ' ' + port
	sock.nlsendto(msg, (TCSip, TCSport))
	print('SUN Msg sent!')
	return msg


def recvSUR():
	if sock.recv(4) == b'SUR ':
		2nd = sock.recv(2)
		if 2nd == 'OK':
			status = 'OK'
			return status
		elif 2nd == 'NO':
			status = 'NOK'
			return status
		else:
			status = 'SUR ERR'
			return status



def parseTRSaddr():
	'''
	Returns port of the TRS server and the name and port of the TCS server connected
	'''
	ap = ArgumentParser()
	ap.add_argument('language', type= str,
		help='Language that the TRS server translates from')
	ap.add_argument('-p', '--port', type=int,
		help='Port number of the TRS server')
	ap.add_argument('-n', '--nameTCS', type=str,
		help='Host name of the listening TCS server')
	ap.add_argument('-e', '--portTCS', type=int,
		help='Port number of the listening TCS server')
	opts = ap.parse_args()
	nameTRS = gethostname()
	lang = args.lang
	port = opts.port if opts.port else 59000
	nameTCS = opts.nameTCS if opts.nameTCS else gethostname()
	portTCS = opts.portTCS if opts.portTCS else 58051
	return (lang, nameTRS, port, nameTCS, portTCS)

def parseSRR():
	sp = unq.split(b' ')
	if len(sp) == 2 and sp[0] == b'SRR' and 
	(sp[1] == b'ERR' or sp[1] == b'OK' or sp[1] == b'ERR') and
	srg.endswith(b'\n'):
		return sp[1].decode()

def parseSUR(TRSsock, TRSaddr):
	return NotImplemented #TODO

def recvTRQ(TRSsock):
	if sock.recv(4) == b'TRQ ':
		2nd = sock.recv(1)
		if 2nd == 't':
			return recvTRRtext()
		elif 2nd == 'f':
			return recvTRRfile()
	return None

	def recvTRQfile():
		filename = b''
		while not filename.endswith(b' '):
			filename += sock.recv(1)
		size = b''
		while not size.endswith(b' '):
			size += sock.recv(1)
		content  = recv(int(size))
		return ('f', filename.decode(), content)
				
	def recvTRQtext():
		words = ()
		N = recv_word(3)
		if not N.isidigit():
			return None
		for _ in range(int(N)):
			words.append(recv_word(LANG_LEN))
		if not recv(1) == b'\n':
			return None
		return words


def main():
	'''
	TRS Execution
	'''
	listener = nlsocket(AF_INET, SOCK_STREAM)
	listener.listen(BACKLOG)
	TRSaddr = parseTRSaddr()

	sendSRG(lang, nameTRS, port)
	recvSRR(status)

	TRSloop(listener)
	#TODO Sair do TRSloop aquando do CTRL+C
	sendSUN(lang, nameTRS, port)
	recvSUR(status)
