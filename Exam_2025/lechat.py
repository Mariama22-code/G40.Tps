import socket
import threading

class LeChat:
    # Q1 - Constructeur
    def __init__(self, max_client, max_message_len, ip_address, port):
        self.max_client = max_client
        self.max_message_len = max_message_len
        self.ip_address = ip_address
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.total_notes = 0
        self.nombre_notes = 0

    # Q2 - manage_connexions
    def manage_connexions(self):
        self.server_socket.bind((self.ip_address, self.port))
        self.server_socket.listen(self.max_client)
        while len(self.clients) < self.max_client:
            client_socket, address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Client connecté : {address}")

    # Q3 - tokenizer
    def tokenizer(self, vocab, message):
        tokens = []
        mots = message.split()
        for mot in mots:
            if mot in vocab:
                tokens.append(vocab[mot])
        return tokens

    # Q4 - handle_client
    def send(self, client_socket, message):
        client_socket.send(message.encode())

    def handle_llm(self, tokens):   # ← ajoute cette fonction
        return "Je suis une IA et voici ma réponse !"

    def handle_client(self, client_id):
        client_socket = self.clients[client_id]
        while True:
            message = client_socket.recv(self.max_message_len).decode()
            if not message.endswith("?") or len(message) > self.max_message_len or "merci" in message:
                self.send(client_socket, "Texte invalide")
                continue
            vocab = {}
            tokens = self.tokenizer(vocab, message)
            reponse = self.handle_llm(tokens)
            self.send(client_socket, reponse)
            # Q5 - Recevoir la note du client
            note = int(client_socket.recv(1024).decode())
            self.total_notes += note
            self.nombre_notes += 1

    # Q5 - get_evaluation
    def get_evaluation(self):
        return self.total_notes / self.nombre_notes

# Pour Lancer le serveur
serveur = LeChat(1, 1024, "127.0.0.1", 8080)
serveur.manage_connexions()
serveur.handle_client(0)