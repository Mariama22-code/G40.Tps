import socket

def serveur():
    host = ''
    port = 8080  # 80 necessite droits admin sur Windows

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    print('Serveur en ecoute sur le port ', port)

    while True:
        c, addr = s.accept()
        print('Connexion de ', addr)

        requete = c.recv(1024).decode('ascii')
        print('Requete recue : ', requete)

        if 'GET /index.html' in requete:
            body = '<!DOCTYPE html>\n<html>\n<body>\n<p>Bonjour</p>\n<p style="font-size:50px;">Cest notre premier serveur</p>\n</body>\n</html>'
            reponse = 'HTTP/1.1 200 OK\r\nServer: PythonTPServer\r\nConnection: Closed\r\n\r\n' + body
        else:
            body = '<html><body><h1>404 Not Found</h1></body></html>'
            reponse = 'HTTP/1.1 404 Not Found\r\nServer: PythonTPServer\r\nConnection: Closed\r\n\r\n' + body

        c.sendall(reponse.encode('ascii'))
        c.close()

if __name__ == '__main__':
    serveur()