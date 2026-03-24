import socket
from _thread import *
import threading

print_lock = threading.Lock()

def communication_client(c):
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
            print_lock.release()
            break

        data = 'Welcome'
        c.send(data.encode())

    # Fermer la connexion
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

        start_new_thread(communication_client, (c,))

    s.close()

if __name__ == '__main__':
    thread_ecoute()