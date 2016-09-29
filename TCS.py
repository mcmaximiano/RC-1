PORT = 58000

from socket import\
        socket,\
        AF_INET,\
        SOCK_STREAM,\
        gethostname

welcome = socket(AF_INET, SOCK_STREAM)
welcome.bind((gethostname(), PORT))
welcome.listen(10)
(serving_socket, client_addr) = welcome.accept()
msg = serving_socket.recv(1000)
welcome.close()
serving_socket.close()
for submsg in msg.split(): 
	print(submsg.decode())
