### Thread : 
Le serveur est mono-tâche, il ne peut gérer qu’un seul client à la fois.
Pour permettre la communication avec plusieurs clients, on utilise des threads. Chaque client est géré dans un thread différent.

--------------------------------------------------------------------------------------------------------------------------------

### Listes des clients : 
### « Quand un client se connecte le serveur lui envoie la liste des clients 
Le serveur maintient une liste des clients connectés. Lorsqu’un nouveau client se connecte, le serveur lui envoie cette liste.
### « notification de déconnexion »
Quand un client se déconnecte, le serveur envoie un message aux autres clients pour les informer.
Ce message peut contenir un texte simple indiquant qu’un client s’est déconnecté.
## « un client choisit son interlocuteur »
Le client choisit à qui envoyer le message. Le serveur reçoit ce message et l’envoie uniquement au client concerné.

-------------------------------------------------------------------------------------------------------------------------------------------------------

## Exercice encoding : 

## Somme nulle de deux
On utilise deux boucles pour tester toutes les paires d’éléments du tableau. Pour chaque paire, on vérifie si la somme est égale à zéro.
## Somme nulle de trois
On utilise trois boucles pour tester toutes les combinaisons de trois éléments. On vérifie si leur somme est égale à zéro.
