import socket
import json

def main():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Message JSON envoye au moment de la connexion
    message = """{
    "nom": "client1",
    "date_connexion": "19/04/2021",
    "lieu": "Paris"
}"""

    s.send(message.encode('ascii'))
    data = s.recv(1024)
    print('message recu du serveur : ', str(data))
    s.close()

if __name__ == '__main__':
    main()