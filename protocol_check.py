class ProtocolError(Exception): pass

def parse_msg(msg, XYZ):
	''' 
	Return the all arguments after the first, making sure that:
	- first argument corresponds to XYZ
	- msg ends in a newline
	- argc corresponds to actual argument count
	'''
	split = msg.split(b' ')
	if split[0] == XYZ.encode() and msg.endswith(b'\n'):
		return split[1:]
	else:
		return None

def parse_ULQ(msg):
	args = parse_all(msg, 'ULQ')
	if len(args) == 0:
		return args
	else:
		return None
	
def parse_ULR(msg):
	"""
	Returns all avaliable languages in a list.
	"""
	# TODO maybe check
	args = parse_all(msg, 'ULR')
	langs = args[1:]
	langc = args[0:1]
	if args is not None and langc.isdigit() and int(langc) == len(langs):
		return langs
	else:
		return None

def parse_UNQ(msg):
	"""
	Returns the requested language.
	"""
	args = parse_all(msg, 'UNQ')
	if len(msg) == 1:
		return args[0]
	else:
		return None
	
def parse_UNR(msg):
	"""
	Returns the requested language.
	"""
	args = parse_all(msgs, 'UNR')


def parse_TRQ(TRQ):
	# XXX special case (sends binary file!): do not use parse_msg
	return NotImplemented

def parse_TRR(TRR):
	# XXX special case (sends binary file!): do not use parse_msg
	return NotImplemented

def parse_SRG():
	return NotImplemented

def parse_SRR():
	return NotImplemented

def parse_SUN():
	return NotImplemented

def parse_SUR():
	return NotImplemented
