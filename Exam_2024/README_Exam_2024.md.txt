import socket
import threading

class Game(object):

    #Q1 - Constructeur (1.5pt) ============
  On définit la classe Game qui représente le serveur de jeu
  Le constructeur sauvegarde les paramètres et crée la socket TCP
    def __init__(self, max_gamers, nbr_sticks):
        self.max_gamers = max_gamers
        self.nbr_sticks = nbr_sticks
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Q2 - Fonction listen (1.5pt) ============
  On ouvre une socket d'écoute et on attend les connexions des joueurs
  On gère le nombre maximum de connexions avec max_gamers
    def listen(self, ip, port):
        self.server_socket.bind((ip, port))
        self.server_socket.listen(self.max_gamers)
        while len(self.clients) < self.max_gamers:
            client_socket, address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Joueur connecté : {address}")

    # Q3 - communicate_with_client (4pt) ============
   On communique avec un joueur particulier
   On vérifie si le choix est valide et on met à jour le nombre de bâtonnets
   Si le joueur tire le dernier bâtonnet il perd et les autres gagnent
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

    # Q4 - Threads + fonction principale (4pt) ============
  On utilise les threads pour gérer plusieurs joueurs en même temps
  Sans threads le serveur bloquerait sur un joueur et les autres attendraient

    # Q5 - UDP vs TCP (1.5pt) ============
   TCP : connexion établie, fiable, données dans l'ordre → SOCK_STREAM
   UDP : pas de connexion, pas fiable, plus rapide → SOCK_DGRAM
   Pour ce jeu TCP est mieux car on a besoin que les messages arrivent dans l'ordre

# Lancer le serveur
game = Game(2, 10)
game.listen("127.0.0.1", 8080)
game.communicate_with_client(0)
game.communicate_with_client(1)