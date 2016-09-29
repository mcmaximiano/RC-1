from socket import socket, AF_INET, SOCK_STREAM
PORT = 58000

def get_input():
        return input('client > ').encode()

msg = get_input()
s = socket(AF_INET, SOCK_STREAM)
s.connect(('guadiana', PORT))
s.send(msg)
s.close()

