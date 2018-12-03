
import socket


mi_socket = socket.socket()

mi_socket.bind(('xxx.xxx.xxx.xxx',7000)) #the ip and the second argument(port) needs to be the same for the client
mi_socket.listen(5)


while(True):
    conexion, addr = mi_socket.accept()

    print("------------")
    print("Nueva conexion establecida!")
    print(addr)
    peticion = conexion.recv(1024).decode()
    print(peticion)
    print("------------\n")

    conexion.sendall("netsh wlan disconnect".encode())
    conexion.close()
