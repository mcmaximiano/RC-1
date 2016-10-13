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
			if type(msg == file)
			# TODO check for file or word translation	
		
		
	

def main():
	listener = nlsocket(AF_INET, SOCK_STREAM)
	listener.listen(BACKLOG)
	TRSloop(listener)
