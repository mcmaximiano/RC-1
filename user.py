#!/usr/bin/python3

from nlsocket import *
from argparse import ArgumentParser
from cmd import Cmd

class Client(Cmd):

	intro = "Welcome to the RC translation client. Type 'help'!"
	prompt = '(RC) '
	TCSsocket = nlsocket(AF_INET, SOCK_DGRAM)  # Must be DGRAM!
	TCS = None # address for the TCS
	languages = None
	
	def __init__(self, TCS):
		super().__init__() # call superclass's constructor
		self.TCS = TCS

	def do_list(self, argv):
		'Query a list of all avaliable languages.'
		self.TCSsocket.nlsendto('ULQ'.encode(), self.TCS)
		msg = msg.split()
		languages = msg[2:]
		for i in range(len(languages)):
			print(i,'>', languages[i])
		self.languages = languages

	def recvULR(self):
		ulr = self.TCSsocket.nlrecv().decode()
		return ulr	
		
	def recvUNR(self):
		unr = self.TCSsocket.nlrecv().decode()
		return unr
			
	def do_request(self, args):
		'Request to connect to a particular TRS.'
		args = args.split()
		langc = int(args[0])
		msg = 'UNQ ' + self.languages[langc]
		msg = msg.encode()
		self.TCSsocket.nlsendto(msg, self.TCS)
		msg = self.TCSsocket.nlrecv()
		print('Got:', msg)

	def do_exit(self, argv):
		'Close the program.'
		self.TCSsocket.close()
		if self.TRS: TRS.close()
		raise SystemExit
	
	def do_EOF(self, argv):
		'Close the program.'
		print()
		self.do_exit(argv)

def parseTCSaddr():
	''' Returns the name and the port number of the TCS server.'''
	ap = ArgumentParser()
	ap.add_argument('-p', '--port', type=int,
		help='Port number of the listening TCS server.')
	ap.add_argument('-n', '--name', type=str,
		help='Host name of the listening TCS server.')
	opts = ap.parse_args()
	name = opts.name if opts.name else gethostname()
	port = opts.port if opts.port else 58051
	return (name, port)

def main():
	TCSaddr = parseTCSaddr()
	client = Client(TCSaddr)
	client.cmdloop()

if __name__ == '__main__': main()
