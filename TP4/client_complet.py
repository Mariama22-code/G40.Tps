import socket
import json

def main():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Message identification envoye a la connexion
    identification = {
        "type": "identification",
        "nom": "client1",
        "date_connexion": "19/04/2021",
        "lieu": "Paris"
    }
    s.send(json.dumps(identification).encode('ascii'))

    # Recevoir la liste des clients connectes
    data = s.recv(1024)
    message = json.loads(data.decode('ascii'))
    print('clients connectes : ', message['clients'])

    while True:
        ans = input('voulez vous continuer ? (y/n) : ')
        if ans == 'y':
            # Notification en train d ecrire
            s.send(json.dumps({
                "type": "notification",
                "evenement": "en_train_ecrire",
                "nom": "client1"
            }).encode('ascii'))

            # Notification changement etat
            s.send(json.dumps({
                "type": "notification",
                "evenement": "changement_etat",
                "nom": "client1", "client2"
                "etat": "OCCUPE"
            }).encode('ascii'))
        else:
            break

    s.close()

if __name__ == '__main__':
    main()