import socket

MAX_BYTES = 65535

class Server:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', port))
        print('En ecoute sur {}'.format(self.sock.getsockname()))

    def run(self):
        while True:
            data, address = self.sock.recvfrom(MAX_BYTES)
            text = data.decode('ascii')
            print('Le client {} dit {!r}'.format(address, text))
            text = 'les donnees ont une taille de {} octets'.format(len(data))
            data = text.encode('ascii')
            self.sock.sendto(data, address)

if __name__ == '__main__':
    server = Server(1060)
    server.run()