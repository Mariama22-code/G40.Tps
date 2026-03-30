import socket
from datetime import datetime

MAX_BYTES = 65535

class Client:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = port

    def run(self):
        text = 'Le temps est  {}'.format(datetime.now())
        data = text.encode('ascii')
        self.sock.sendto(data, ('127.0.0.1', self.port))
        print('mon adresse est {}'.format(self.sock.getsockname()))
        data, address = self.sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        self.sock.sendto(data, address)

if __name__ == '__main__':
    client = Client(1060)
    client.run()