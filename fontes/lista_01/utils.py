
import socket
import pickle
from threading import Thread
from models import CalculadoraNotas


class Worker(Thread):
    def __init__(self, conn, client):
        Thread.__init__(self)
        self.conn = conn
        self.client = client

    def run(self):
        dados = self.conn.recv(1024)
        dados = pickle.loads(dados)
        if dados['op'] == 'media':
            calculadora = CalculadoraNotas()
            notas = dados['dados']
            media = calculadora.calculaAprovacao(notas)
            print('Enviando ', media, 'para  cliente')
            self.conn.send(pickle.dumps(media))
            self.conn.close()
        elif dados['op'] == 'maioridade':
            pessoa = dados['dados']
            maioridade = pessoa.is_maior()
            print('Enviando ', maioridade, 'para  cliente')
            self.conn.send(pickle.dumps(maioridade))
            self.conn.close()





class ClienteSocket(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def enviar(self, dados):
        try:
            self.client.send(dados)
            return 0
        except Exception as e:
            return e

    def recebe(self):
        return self.client.recv(1024)




class ServerSocket(object):
    def __init__(self, host, port, protocolo):
        self.clients = []
        if protocolo.lower() == 'tcp':
            self.chanel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocolo.lower() == 'udp':
            self.chanel = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.chanel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chanel.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.chanel.bind((host, port))
        self.chanel.listen(10)
        # Define um limite máximo para conexoes
        self.MAX_CONN = 20
        self.countConn = 0

    def listener(self):
        while self.countConn < self.MAX_CONN:
            try:
                conn, client = self.chanel.accept()
                self.countConn += 1
                print('Conexão estabelecida!!')
                # criar thread para tratar solicitação
                worker = Worker(conn, client)
                worker.start()
            except KeyboardInterrupt:
                exit(0)
