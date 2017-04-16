import socket

def Main():

    host = '127.0.0.1'
    port = 5021
    usuario=input('Ingrese Usuario->')     
    while 1:
        try:
            mySocket = socket.socket();
            mySocket.connect((host,port))
            mySocket.send(usuario.encode())
            print(mySocket.recv(1024).decode())
            break  
        except socket.error:
            pass
        except socket.timeouterror:
            break
         
    mySocket.close()

if __name__ == '__main__':
    Main()


#message = input(" -> ")
                    #mySocket.send(message.encode())

                