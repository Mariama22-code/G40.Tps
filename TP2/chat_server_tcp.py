import socket

HOST = '127.0.0.1'
PORT = 1060

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

print('Serveur de chat TCP en ecoute sur', HOST, PORT)
conn, addr = s.accept()
print('Client connecte depuis', addr)

while True:
    data = conn.recv(1024)
    if not data:
        print('Client deconnecte')
        break
    print('Client : ', data.decode('ascii'))
    message = input('Serveur : ')
    conn.sendall(message.encode('ascii'))

conn.close()
s.close()