def formater_reponse(version, status_code, status_text, headers, body):
    if version == 1:
        version_str = 'HTTP/1.1'
    else:
        version_str = 'HTTP/2.0'

    reponse = version_str + ' ' + str(status_code) + ' ' + status_text + '\r\n'

    for nom, valeur in headers.items():
        reponse = reponse + nom + ': ' + valeur + '\r\n'

    reponse = reponse + '\r\n'
    reponse = reponse + body

    return reponse

if __name__ == '__main__':
    headers = {'Server': 'PythonTPServer', 'Connection': 'Closed'}
    body = '<html><body><h1>404 Not Found</h1></body></html>'
    print(formater_reponse(1, 404, 'Not Found', headers, body))