from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import socket
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:(escribir password)@127.0.0.1'
db = SQLAlchemy(app)
db.engine.execute('CREATE DATABASE IF NOT EXISTS ore;')
db.engine.execute('USE ore;')
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True)
db.create_all()
def Main():
    host = "127.0.0.1"
    port = 5021
    while True:
        mySocket = socket.socket()
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((host,port))
        mySocket.listen(1)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        data = str(data)
        if db.session.query(Usuarios.id).filter_by(usuario=data).scalar() is None:
            usuario = Usuarios()
            usuario.usuario = data
            db.session.add(usuario)
            db.session.commit()
            conn.send('Dato Guardado'.encode())
        else:
            conn.send('Dato Ya existente'.encode()) 

        conn.close()
        mySocket.close()    
            #if not data:
               
    
if __name__ == '__main__':
    Main()
