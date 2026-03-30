import socket
from _thread import *
import threading
import json

print_lock = threading.Lock()
clients_connectes = {}

def notifier_tous(message, exclude=None):
    for nom, conn in clients_connectes.items():
        if nom != exclude:
            try:
                conn.send(json.dumps(message).encode('ascii'))
            except:
                pass

def communication_client(c):
    nom_client = None
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            # Notification deconnexion
            if nom_client and nom_client in clients_connectes:
                del clients_connectes[nom_client]
                notifier_tous({
                    "type": "notification",
                    "evenement": "client_deconnecte",
                    "nom": nom_client
                })
            break

        message = json.loads(data.decode('ascii'))

        # Message identification
        if message['type'] == 'identification':
            nom_client = message['nom']
            clients_connectes[nom_client] = c
            print('nom du client : ', message['nom'])
            print('lieu de connexion : ', message['lieu'])

            # Envoyer la liste des clients connectes
            liste = list(clients_connectes.keys())
            c.send(json.dumps({
                "type": "notification",
                "evenement": "nombre_clients",
                "clients": liste
            }).encode('ascii'))

            # Notifier les autres
            notifier_tous({
                "type": "notification",
                "evenement": "client_connecte",
                "nom": nom_client
            }, exclude=nom_client)

        # Message notification etat
        elif message['type'] == 'notification':
            if message['evenement'] == 'changement_etat':
                print(message['nom'], ' est maintenant ', message['etat'])
                notifier_tous(message, exclude=nom_client)

            elif message['evenement'] == 'en_train_ecrire':
                notifier_tous(message, exclude=nom_client)

    c.close()

def thread_ecoute():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket bindee au port ", port)

    s.listen(5)
    print("le serveur est en ecoute...")

    while True:
        c, addr = s.accept()

        print_lock.acquire()
        print('Connecte au client : ', addr[0], ':', addr[1])
        print_lock.release()

        start_new_thread(communication_client, (c,))

    s.close()

if __name__ == '__main__':
    thread_ecoute()