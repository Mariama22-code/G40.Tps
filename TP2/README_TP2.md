# TP2 — UDP vs TCP

**Nom :** Mariama Abdourahamane Kassoum  
------------------------------------------------------------------------------------------------------------------------------------------------------

## Différences UDP vs TCP

| UDP | TCP |
|---|---|
| Mode non connecté | Mode connecté |
| Pas d'ordre de réception | Paquets rangés dans l'ordre |
| Entête de 8 octets | Entête de 20 octets |
| Pas d'accusé de réception | Accusé de réception |
| Pas de handshake | Protocole de handshake |
| Acheminement non garanti | Fiabilité garantie |

----------------------------------------------------------------------------------------------------------------------------------------------------

## Exercice 1 — Réécriture en classes

Le serveur TCP et le client TCP ont été réécrits en classes. Le polymorphisme peut être utilisé en créant une classe mère commune dont héritent les classes Server et Client.

---

## Exercice 2 — Argparse

La librairie argparse permet de n'utiliser qu'un seul fichier pour le serveur et le client en ajoutant un argument qui permet de choisir le mode d'exécution.

--------------------------------------------------------------------------------------------------------------------------------------------

## Exercice 3 — Librairie sys

La librairie sys permet de lire le message tapé par l'utilisateur dans l'invite de commande au lieu d'envoyer un message fixe.

-----------------------------------------------------------------------------------------------------------------------------------------------

## Application de chat — UDP ou TCP ?

TCP est mieux adapté pour notre application de chat car :
- Il garantit la fiabilité de la transmission des messages
- Les messages arrivent dans l'ordre d'envoi
- Il détecte les déconnexions des clients
- Il garantit qu'aucun message n'est perdu

--------------------------------------------------------------------------------------------------------------------------------------------

## Exercice de coding — Contient il des doublons :

On parcourt le tableau et on vérifie si un élément apparaît plus d'une fois.

**Résultats :**
- `[1, 2, 3, 1]` : `True`
- `[1, 2, 3, 4]` :`False`

--------------------------------------------------------------------------------------------------------------------------

## Des anagrammes :

On trie les deux chaînes et on compare. Si elles sont égales après tri, c'est un anagramme.

**Résultats :**
- `s = python, t = onhtyp` → `True`
- `s = tp, t = tps` → `False`
