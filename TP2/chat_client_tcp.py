import socket

HOST = '127.0.0.1'
PORT = 1060

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Connecte au serveur de chat TCP')

while True:
    message = input('Client : ')
    s.sendall(message.encode('ascii'))
    data = s.recv(1024)
    if not data:
        print('Serveur deconnecte')
        break
    print('Serveur : ', data.decode('ascii'))

s.close()