import socket
import xml.etree.ElementTree as ET

def main():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Message XML envoye au moment de la connexion
    message = """<client>
    <nom>client1</nom>
    <date_connexion>19/04/2021</date_connexion>
    <lieu>Paris</lieu>
</client>"""

    s.send(message.encode('ascii'))
    data = s.recv(1024)
    print('message recu du serveur : ', str(data))
    s.close()

if __name__ == '__main__':
    main()