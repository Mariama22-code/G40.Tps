import socket
import sys

HOST = '127.0.0.1'
PORT = 1060

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print('le serveur ecoute sur ', HOST, PORT)
    sc, sockname = s.accept()
    print('Client connecte depuis ', sockname)
    data = sc.recv(1024)
    print('Message recu : ', data.decode('ascii'))
    sc.sendall(b'Au revoir !')
    sc.close()
    s.close()

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('Connecte depuis ', s.getsockname())
    print("Entrez votre message : ")
    message = sys.stdin.readline().strip()
    s.sendall(message.encode('ascii'))
    data = s.recv(1024)
    print('Le serveur a repondu : ', data.decode('ascii'))
    s.close()

if __name__ == '__main__':
    if sys.argv[1] == 'serveur':
        server()
    else:
        client()