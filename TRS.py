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

def TRSloop(listener):
	while 1:
		(server, clientaddr) = listener.accept()
		msg = recvTRQ(listener)
			if (msg[0] == t):
				msg_len = str(len(msg)-1)
				answer = 'TRR ' + msg[0] + ' ' + msg_len
				for el in msg[1:]
					answer += ' ' +  get_word_trans('text_translation.txt', el)
				print('Sending:\n' + answer + '\n...to:', listener)
				answer = answer.encode()
				self.sock.nlsendto(answer,listener)
				print('Message sent!')
			# TODO translate words
			elif (msg[0] == f):
				filename = msg[1]
				trans_file_name = get_image_trans_filename('file_translation.txt', filename)
				answer_file = open(trans_file_name, 'rb')
				data = file.read()
				size = len(conteudo)
				answer = 'TRR ' + msg[0] + ' ' + trans_file_name + ' ' + bytes[size] + ' ' + data 
				print('Sending file:\n' + trans_file_name + '\n...to:', listener) 
				answer = answer.encode()
				self.sock.nlsendto(answer, listener)
				print('File sent!')
			# TODO translate file
			else return 'TRQ ERR'
				
		
		
	

def main():
	listener = nlsocket(AF_INET, SOCK_STREAM)
	listener.listen(BACKLOG)
	TRSloop(listener)
