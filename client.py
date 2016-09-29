from socket import socket, AF_INET, SOCK_STREAM
PORT = 58000

msg = b'ola'
s = socket(AF_INET, SOCK_STREAM)
s.connect(('guadiana', PORT))
s.send(msg)
s.close()

def get_input():
        return input().split()
