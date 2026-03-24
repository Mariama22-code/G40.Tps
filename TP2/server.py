import socket

HOST = '127.0.0.1'
PORT = 1060

def recv_all(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more
    return data

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        print('le serveur ecoute a cette adresse ', s.getsockname())
        sc, sockname = s.accept()
        print('Le serveur a accepte une connection de ', sockname)
        message = recv_all(sc, 9)
        print('Message recu : ', repr(message))
        sc.sendall(b'Au revoir !')
        sc.close()
        print("Reponse envoyee, socket fermee")

if __name__ == '__main__':
    server()