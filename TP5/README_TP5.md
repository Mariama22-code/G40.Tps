# TP5 — Raw Socket et modèle OSI

\*\*Nom :\*\* Mariama Abdourahamane Kassoum  
------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Erreurs trouvées et corrections

### Erreur 1 — ip\_tot\_len non définie

\*\*Problème :\*\*
Dans le code source, la variable utilisée dans le pack s'appelle `ip\_tot\_len` mais elle a été définie sous le nom `ip\_total\_len`. Python ne trouve pas la variable et lève une NameError.

\*\*Correction :\*\*
Remplacer `ip\_tot\_len` par `ip\_total\_len` dans le pack pour que le nom corresponde à la variable définie.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### Erreur 2 — Fonction checksum non définie

\*\*Problème :\*\*
La fonction `checksum` est appelée dans `create\_tcp\_header` pour calculer la somme de contrôle du paquet mais elle n'as pas été définie dans le code source. Cela provoque une NameError à l'exécution.

\*\*Correction :\*\*
Définir la fonction `checksum` qui parcourt le pseudo-header par paires d'octets, additionne les valeurs et retourne le complément à un du résultat

-----------------------------------------------------------------------------------------------------------------------------------------------------------
### Erreur 3 — Fonction create\_packet non définie
\*\*Problème :\*\*
La fonction `create\_packet` est appelée dans la fonction principale mais elle n'est jamais définie dans le code source. Cela provoque une également une NameError à l'exécution.

\*\*Correction :\*\*
Définir la fonction `create\_packet` qui assemble l'entête IP, l'entête TCP et le message encodé en bytes et retourne la concaténation des trois.
\------------------------------------------------------------------------------------------------------------------------------------------
### Erreur 4 — Raw socket bloquée sur Windows

*\*Problème :\*\*

Les raw sockets avec IPPROTO\_RAW sont bloquées sur Windows pour des raisons de sécurité. Même avec les droits administrateur, Windows interdit l'envoi de paquets via une raw socket. Cela provoque une **PermissionError** à l'exécution.

\*\*Pourquoi cette erreur ne peut pas être résolue :\*\*
Cette restriction est imposée directement par Microsoft au niveau du système d'exploitation. Aucune modification du code Python ne peut contourner cette limitation. La seule solution est d'utiliser un système Linux qui autorise les raw sockets avec les droits root.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Limites des Raw Sockets

- **Windows bloque les raw sockets** : Microsoft interdit leur utilisation pour des raisons de sécurité, même avec les droits administrateur. Impossible d'envoyer des paquets raw sur Windows.
- **Droits root obligatoires sur Linux** : Sur Linux, les raw sockets nécessitent obligatoirement les droits root. Un utilisateur normal ne peut pas les utiliser.
- **Construction manuelle des entêtes** : Avec les raw sockets, le développeur doit construire manuellement les entêtes IP et TCP, ce qui est complexe et source d'erreurs.
- **Pas de gestion automatique des erreurs** : Contrairement à TCP, les raw sockets ne gèrent pas automatiquement les retransmissions, l'ordre des paquets ou les accusés de réception.
- **Difficulté de débogage** : Les erreurs au niveau des entêtes sont difficiles à détecter car le système ne remonte pas d'erreurs explicites.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Comparatif Raw Socket vs TCP vs UDP

| Critère | Raw Socket | TCP (SOCK_STREAM) | UDP (SOCK_DGRAM) |
|---|---|---|---|
| Couche OSI | Couche 3 (Réseau) | Couche 4 (Transport) | Couche 4 (Transport) |
| Mode connexion | Aucun protocole imposé | Mode connecté | Mode non connecté |
| Entête | Construite manuellement | Gérée automatiquement | Gérée automatiquement |
| Fiabilité | Non garantie | Garantie | Non garantie |
| Accusé de réception | Non | Oui | Non |
| Ordre des paquets | Non garanti | Garanti | Non garanti |
| Complexité | Très élevée | Faible | Faible |
| Utilisation | Analyse réseau, outils type Wireshark | Chat, HTTP, FTP | Streaming, jeux en ligne |
| Windows | Bloqué | Autorisé | Autorisé |
| Linux | Autorisé (root) | Autorisé | Autorisé |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Application de chat — Modification des clients
Le code source des clients des TPs précédents a été modifié pour utiliser une raw socket au lieu de SOCK\_DGRAM ou SOCK\_STREAM.
Pour chaque client, la modification consiste à :
- Construire manuellement l'entête IP avec create\_ip\_header
- Construire manuellement l'entête TCP avec create\_tcp\_header
- Assembler le paquet avec create\_packet
- Remplacer la socket par SOCK\_RAW

### client\_raw\_tp1.py
Le client UDP du TP1 a été modifié pour envoyer le message de date/heure via une raw socket.
### client\_raw\_tp2.py
Le client TCP du TP2 a été modifié pour envoyer le message via une raw socket.
### client\_raw\_tp3.py
Le client TCP avec threads du TP3 a été modifié pour envoyer le message via une raw socket.
### client\_raw\_tp4.py
Le client JSON du TP4 a été modifié pour envoyer le message JSON via une raw socket.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Exercice de coding — Nombre de bits à 1
On parcourt la représentation binaire du nombre. Pour chaque bit, si sa valeur est 1 on incrémente le compteur.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Swap bits
On récupère les bits aux positions i et j. Si les deux bits sont différents on les échange, sinon le nombre reste identique.

