def formater_requete(methode, url, version, headers, body):
    methodes_valides = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']

    if methode not in methodes_valides:
        return 'Methode HTTP invalide'

    if version == 1:
        version_str = 'HTTP/1.1'
    else:
        version_str = 'HTTP/2.0'

    requete = methode + ' ' + url + ' ' + version_str + '\r\n'

    for nom, valeur in headers.items():
        requete = requete + nom + ': ' + valeur + '\r\n'

    requete = requete + '\r\n'
    requete = requete + body

    return requete

if __name__ == '__main__':
    headers = {'Host': 'localhost:8000', 'User-Agent': 'Mozilla/5.0'}
    print(formater_requete('GET', '/index.html', 1, headers, ''))