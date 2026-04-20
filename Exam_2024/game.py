import socket
import threading

class Game(object):
    def __init__(self, max_gamers, nbr_sticks):
        self.max_gamers = max_gamers
        self.nbr_sticks = nbr_sticks
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self, ip, port):
        self.server_socket.bind((ip, port))
        self.server_socket.listen(self.max_gamers)
        while len(self.clients) < self.max_gamers:
            client_socket, address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Joueur connecté : {address}")

    def send(self, client_id, message):
        self.clients[client_id].send(message.encode())

    def read(self, client_id):
        return self.clients[client_id].recv(1024).decode()

    def communicate_with_client(self, client_id: int) -> None:
        self.send(client_id, f"Il reste {self.nbr_sticks} bâtonnets")
        self.send(client_id, "Choisissez 1, 2 ou 3 bâtonnets à retirer")
        reponse = self.read(client_id)
        if not reponse.isdigit() or int(reponse) < 1 or int(reponse) > 3:
            self.send(client_id, "Erreur : choisissez 1, 2 ou 3")
            return
        self.nbr_sticks -= int(reponse)
        if self.nbr_sticks > 0:
            self.send(client_id, "Vous restez dans le jeu")
        else:
            self.send(client_id, "perdu")
            for i in range(len(self.clients)):
                if i != client_id:
                    self.send(i, "gagné")

game = Game(2, 10)
game.listen("127.0.0.1", 8080)

game.communicate_with_client(0)  # joueur 0 joue en premier
game.communicate_with_client(1)  # joueur 1 joue ensuite