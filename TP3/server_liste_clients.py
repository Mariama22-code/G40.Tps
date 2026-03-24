import socket
from _thread import start_new_thread
import threading

print_lock = threading.Lock()
clients = {}  # {socket: nom_client}

# Envoie la liste des clients connectés à un client
def envoyer_liste_clients(c):
    if clients:
        c.send(("Clients connectés : " + ", ".join(clients.values())).encode())
    else:
        c.send("Aucun client connecté pour le moment".encode())

# Notifie tous les autres clients qu'un nouveau client s'est connecté
def notifier_connexion(nom):
    message = f"{nom} a rejoint le chat !"
    for client_socket, client_nom in clients.items():
        if client_nom != nom:
            try:
                client_socket.send(message.encode())
            except:
                pass

# Notifie tous les clients qu'un client s'est déconnecté
def notifier_deconnexion(nom, socket_deconnectee):
    message = f"{nom} s'est déconnecté."
    for client_socket in clients:
        if client_socket != socket_deconnectee:
            try:
                client_socket.send(message.encode())
            except:
                pass

# Communication avec un client
def communication_client(c):
    nom = None
    try:
        # Demander le nom du client
        c.send("Entrez votre nom : ".encode())
        nom = c.recv(1024).decode().strip()

        with print_lock:
            clients[c] = nom
            envoyer_liste_clients(c)  # Envoie la liste au nouveau client
            notifier_connexion(nom)   # Notifie les autres clients
            print(f"{nom} s'est connecté.")

        # Boucle de réception des messages
        while True:
            data = c.recv(1024)
            if not data:
                break

            message = data.decode().strip()

            # Si le client tape 'quit', on sort
            if message.lower() == "quit":
                break

            # Format attendu : destinataire:message
            if ":" in message:
                destinataire, contenu = message.split(":", 1)
                destinataire = destinataire.strip()
                contenu = contenu.strip()
                envoye = False

                for client_socket, client_nom in clients.items():
                    if client_nom == destinataire:
                        try:
                            client_socket.send(f"[{nom}] : {contenu}".encode())
                            envoye = True
                        except:
                            pass
                        break

                if not envoye:
                    c.send(f"Client '{destinataire}' introuvable.".encode())
            else:
                c.send("Format invalide. Utilisez 'destinataire:message'".encode())

    except ConnectionResetError:
        print(f"Connexion coupée brutalement par {nom}.")
    except Exception as e:
        print(f"Erreur avec le client {nom} : {e}")
    finally:
        with print_lock:
            if c in clients:
                nom_client = clients[c]
                del clients[c]
                notifier_deconnexion(nom_client, c)
                print(f"{nom_client} s'est déconnecté.")
        c.close()

# Thread principal du serveur
def thread_ecoute():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket bindée au port", port)

    s.listen(5)
    print("Le serveur est en écoute...")

    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print("Connecté au client :", addr[0], ":", addr[1])
        start_new_thread(communication_client, (c,))
        print_lock.release()

if __name__ == '__main__':
    thread_ecoute()