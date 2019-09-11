import socket
import pickle
from threading import Thread
import socket
import pickle
from utils.connectSockt import ServerSocket

class Pessoa(object):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    
    def is_maior(self):
        if str(self.sexo).lower() == 'f' and self.idade >= 21:
            return True
        elif str(self.sexo).lower() == 'm' and self.idade >= 18:
            return True
        elif str(self.sexo).lower() not in ['f', 'm']:
            return 'Sexo inválido'
        else:
            return False

class Worker(Thread):
    def __init__(self, conn, client):
        Thread.__init__(self)
        self.conn = conn
        self.client = client

    
    def run(self):
        content = self.conn.recv(1024)
        pessoa = pickle.loads(content)

        self.conn.send(pickle.dumps(pessoa.is_maior()))


serverSocket = ServerSocket('localhost', 3000, 'tcp')
serverSocket.listener()

