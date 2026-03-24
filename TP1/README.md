# G40.Tps
Nom : Mariama Abdourahamane Kassoum  
---------------------------------------------------------------------------------------------------
### TP1 :
## Response 1 — Les deux scripts:

### server.py
Le serveur crée une socket UDP liée sur 127.0.0.1:1060. Il attend en boucle infinie des messages de clients.
Quand il reçoit un message, il l'affiche avec l'adresse du client et répond avec la taille en octets du message reçu.

### client.py
Le client crée une socket UDP, envoie la date et l'heure actuelle au serveur sur `127.0.0.1:1060`, affiche sa propre adresse socket et reçoit la réponse du serveur.

-------------------------------------------------------------------------------------------------------

## Response 2 — Les fonctions utilisées :

| Fonction | Rôle |
|---|---|
| `socket.socket(AF_INET, SOCK_DGRAM)` | Crée une socket UDP |
| `sock.bind((ip, port))` | Lie la socket à une adresse (serveur) |
| `sock.recvfrom(MAX_BYTES)` | Reçoit données + adresse expéditeur |
| `sock.sendto(data, address)` | Envoie des données vers une adresse |
| `sock.getsockname()` | Retourne l'adresse locale de la socket |
| `data.encode('ascii')` | Convertit str → bytes |
| `data.decode('ascii')` | Convertit bytes → str |

---------------------------------------------------------------------------------------------------------

## Response 3 — Réécriture en classes

Les deux programmes ont été réécrits en utilisant des classes Python : 
### server_class.py contient la classe **Server** avec les méthodes __init__ et run
### client_class.py contient la classe **Client** avec les méthodes __init__ et run

-----------------------------------------------------------------------------------------------------------

## Chat entre deux clients

### Response 1 — Modifications proposées pour N clients

Pour qu'un client A puisse discuter directement avec un client B :
- Le serveur stocke l'adresse de chaque client dans une liste
- Quand un client envoie un message, le serveur le retransmet à tous les autres clients de la liste
- Le client peut saisir un message manuellement avec input()

### Response 2 — Inconvénients de cette architecture

- Le serveur est un **point unique de défaillance** : si le serveur tombe, toute la communication est interrompue.
- Tous les messages passent par le serveur, ce qui crée un **goulot d'étranglement** si le nombre de clients augmente.
- La communication n'est pas **directe** entre les clients, ce qui ajoute de la latence.
- Le serveur doit gérer **N canaux simultanément**, ce qui devient complexe avec beaucoup de clients.

## Exercice de coding — Produit des autres éléments

Pour chaque indice 'i', on multiplie tous les éléments du tableausauf celui à la position 'i' en utilisant une double boucle, sans division.
**Résultats :**
- [1, 2, 3, 4, 5] : [120, 60, 40, 30, 24]
- [3, 2, 1] : 
