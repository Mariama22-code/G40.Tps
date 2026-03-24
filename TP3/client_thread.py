import socket

def main():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = 'Bonjour, je suis un nouveau client'
    while True:
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('message recu du serveur : ', str(data))
        ans = input('voulez vous continuer ?')
        if ans == 'y':
            continue
        else:
            break

    s.close()

if __name__ == '__main__':
    main()