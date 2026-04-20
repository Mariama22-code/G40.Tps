import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))
print("Connecté au serveur !")

while True:
    message = input("Votre question : ")
    client.send(message.encode())
    
    reponse = client.recv(1024).decode()
    print(f"Serveur : {reponse}")
    
    if reponse == "Texte invalide":
        continue
    
    note = input("Donnez une note (0-10) : ")
    client.send(note.encode())

client.close()