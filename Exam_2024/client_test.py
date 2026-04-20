import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

while True:
    message = client.recv(1024).decode()
    print(f"Serveur : {message}")
    
    if message == "perdu" or message == "gagné":
        break
    
    choix = input("Votre choix (1, 2 ou 3) : ")
    client.send(choix.encode())

client.close()