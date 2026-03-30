import socket

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('En ecoute sur {}'.format(sock.getsockname()))
    
    clients = []  # liste pour stocker les adresses des clients
    
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('Le client {} dit {!r}'.format(address, text))
        
        # on ajoute le client s'il n'est pas encore dans la liste
        if address not in clients:
            clients.append(address)
        
        # on retransmet le message à tous les autres clients
        for client in clients:
            if client != address:
                sock.sendto(data, client)

if __name__ == '__main__':
    server(1060)