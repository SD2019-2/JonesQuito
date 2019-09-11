import socket
import pickle
import importlib
from threading import Thread
importlib.find_loader('Pessoa', ['../models/pessoa'])

class Worker(Thread):
    def __init__(self, conn, client):
        Thread.__init__(self)
        self.conn = conn
        self.client = client

    
    def run(self):
        content = self.conn.recv(1024)
        pessoa = pickle.loads(content)

        self.conn.send(pickle.dumps(pessoa.is_maior()))