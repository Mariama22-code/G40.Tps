import socket
import argparse

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
        print('Une connexion : ', sc.getsockname(), ' et ', sc.getpeername())
        message = recv_all(sc, 9)
        print('Les 16 octets recu : ', repr(message))
        sc.sendall(b'Au revoir !')
        sc.close()
        print("Une reponse a ete envoye, la socket est fermee")

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('Le serveur a assigne {} comme socket pour le client'.format(s.getsockname()))
    s.sendall(b'Bonjour !')
    reply = recv_all(s, 11)
    print('Le serveur a repondu : ', repr(reply))
    s.close()

if __name__ == '__main__':
    # creation de l'objet parser
    choices = ['serveur', 'client']
    parser = argparse.ArgumentParser(description='Programme de test de parcours des arguments')
    parser.add_argument('choix', choices=choices, help='choix du programme')
    parser.add_argument('-d', metavar='DECIMAL', type=int, default=40, help='nombre de calcul')

    # creation de l'objet des arguments parse tel qu'entre par l'utilisateur
    args = parser.parse_args()

    print('le choix entre est ', args.choix)
    print('le decimal entre est ', args.d)

    if args.choix == 'serveur':
        server()
    else:
        client()