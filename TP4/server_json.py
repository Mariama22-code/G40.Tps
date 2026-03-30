import socket
from _thread import *
import threading
import json

print_lock = threading.Lock()

def communication_client(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            break

        # Lecture du message JSON
        client = json.loads(data.decode('ascii'))
        print('nom du client : ', client['nom'])
        print('lieu de connexion : ', client['lieu'])

        c.send('Welcome'.encode())

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