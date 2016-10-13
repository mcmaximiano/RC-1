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


def sendSRG(language, IPTRS, portTRS):
	
	
	return NotImplemented


def recvSRR():
	return NotImplemented


def sendSUN():
	return NotImplemented


def redcv():
	return NotImplemented


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
	lang = args.lang
	port = opts.port if opts.port else 59000
	nameTCS = opts.nameTCS if opts.nameTCS else gethostname()
	portTCS = opts.portTCS if opts.portTCS else 58051
	return (lang, port, nameTCS, portTCS)




def main():
	'''
	TRS Execution
	'''
	listener = nlsocket(AF_INET, SOCK_STREAM)
	listener.listen(BACKLOG)
	TRSaddr = parseTRSaddr()

	sendSRG(lang, iptrs, port)
	recvSRR(status)	

	TRSloop(listener)

	sendSUN(language, iptrs, porttrs)
	recvSUR(status)



























