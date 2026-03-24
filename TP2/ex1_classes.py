import socket
import sys

HOST = '127.0.0.1'
PORT = 1060

class SocketBase:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def recv_all(self, sock, length):
        data = b''
        while len(data) < length:
            more = sock.recv(length - len(data))
            if not more:
                raise EOFError('la socket a ete fermee')
            data += more
        return data

    def run(self):
        raise NotImplementedError

class Serveur(SocketBase):
    def run(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        while True:
            print('le serveur ecoute a cette adresse ', self.s.getsockname())
            sc, sockname = self.s.accept()
            print('Le serveur a accepte une connection de ', sockname)
            message = self.recv_all(sc, 9)
            print('Message recu : ', repr(message))
            sc.sendall(b'Au revoir !')
            sc.close()
            print("Reponse envoyee, socket fermee")

class Client(SocketBase):
    def run(self):
        self.s.connect((self.host, self.port))
        print('Connecte depuis ', self.s.getsockname())
        self.s.sendall(b'Bonjour !')
        reply = self.recv_all(self.s, 11)
        print('Le serveur a repondu : ', repr(reply))
        self.s.close()

if __name__ == '__main__':
    if sys.argv[1] == 'serveur':
        Serveur(HOST, PORT).run()
    else:
        Client(HOST, PORT).run()