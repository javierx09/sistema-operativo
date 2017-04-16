from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import socket
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:92wzjpow@127.0.0.1/testo'
db = SQLAlchemy(app)
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True)
db.create_all()
def Main():
    host = "127.0.0.1"
    port = 5011
    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            data = str(data)
            if db.session.query(Usuarios.id).filter_by(usuario=data).scalar() is None:
                    usuario = Usuarios()
                    usuario.usuario = data
                    db.session.add(usuario)
                    db.session.commit()
                    msg='Dato Guardado'
                    conn.send(msg.encode())
                    break
            else:
                    conn.send('Dato Ya existente'.encode()) 
                    break

            if not data:
                    break
            

    conn.close()

if __name__ == '__main__':
    Main()
