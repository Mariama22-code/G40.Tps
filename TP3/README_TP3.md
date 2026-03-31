# TP3 — Premier Serveur Multi-Thread

**Nom :** Mariama Abdourahamane Kassoum  
---------------------------------------------------------------------------------------------------------------------------------------------------------

## Mise en situation

Le serveur du TP précédent est mono-tâche : il ne peut répondre qu'à un seul client à la fois. Pour le rendre multi-tâche, on utilise des **threads** qui tournent au sein du même processus.
Chaque client connecté dispose de son propre thread de communication.

---

## Le serveur — Deux fonctions principales

### thread_ecoute()
Crée la socket TCP (`SOCK_STREAM`) liée au port `12345`, écoute les connexions entrantes avec `s.listen(5)` et crée un nouveau thread pour chaque client avec `start_new_thread`.

### communication_client(c)
Tourne dans un thread dédié par client. Reçoit les données du client avec `c.recv(1024)`. Répond `Welcome` au client. Quand le client ferme la socket, il n'y a plus de données
(`if not data`) : on affiche `Bye` et on ferme la connexion.

### print_lock
Verrou `threading.Lock()` utilisé pour éviter que plusieurs threads n'écrivent en même temps dans le terminal.

------------------------------------------------------------------------------------------------------------------------------------------------

## Exercice — Réécriture en classe

Le code du serveur a été regroupé dans une classe comme pour les TP précédents, avec les méthodes `communication_client` et `thread_ecoute`.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Liste des clients

### Question 1 — Envoyer la liste des clients connectés
Quand un client se connecte, le serveur lui envoie la liste des adresses des clients déjà connectés, stockée dans un dictionnaire `clients`.

### Question 2 — Notification de déconnexion
Quand un client se déconnecte, le serveur envoie une notification à tous les autres clients contenant :
- L'adresse du client déconnecté
- Un message indiquant qu'il s'est déconnecté

### Question 3 — Choisir son interlocuteur
Au moment de l'envoi d'un message, le client choisit son interlocuteur. Le serveur retransmet le message uniquement au client destinataire en parcourant le dictionnaire `clients`.

-------------------------------------------------------------------------------------------------------------------------------------------

## Exercice de coding — Somme nulle de deux

On parcourt le tableau avec deux boucles imbriquées. Pour chaque paire d'éléments, si leur somme est égale à zéro on ajoute la paire au résultat.
Plus le tableau est grand, plus le nombre de comparaisons augmente car on compare chaque élément avec tous les autres.

**Résultat :**
- `[1, 20, 15, 3, 5, -3, 41]` : `[3, -3]`

## Somme nulle de trois

Même principe avec trois boucles imbriquées. Pour chaque triplet `(i, j, k)`, si la somme des trois éléments est nulle on ajoute le triplet au résultat.
La complexité augmente par rapport à la somme de deux car on ajoute une boucle supplémentaire. On peut améliorer la solution en utilisant un ensemble
pour stocker les valeurs déjà vues et éviter la troisième boucle.

**Résultat :**
- `[1, 20, 15, 3, 5, -4, 41]` : `[1, 3, -4]`
