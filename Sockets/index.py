import socket

socket_family = ''
socket_type = ''

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s = ''
#connessione a google
serversocket.connect(("www.lastampa.it", 80))

serversocket.bind((socket.gethostname(), 80))
#socket server
serversocket.listen(5)

serversocket = s

print(s, '/n')

