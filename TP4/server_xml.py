import socket
from _thread import *
import threading
import xml.etree.ElementTree as ET

print_lock = threading.Lock()

def communication_client(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            break

        # Lecture du message XML
        root = ET.fromstring(data.decode('ascii'))
        print('nom du client : ', root[0].text)
        print('lieu de connexion : ', root[2].text)

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