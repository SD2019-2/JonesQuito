import socket
import pickle

from models.pessoa import Pessoa
from utils.connectSockt import ClienteSocket

pessoa = Pessoa('Leandra', 25, 'f')
pessoa = pickle.dumps(pessoa)

cliente = ClienteSocket('localhost', 3000)
cliente.enviar(pessoa)

print('antes de conectar!')
resposta = pickle.loads(cliente.recebe())
if resposta:
    print(pickle.loads(pessoa).nome, 'é maior de idade')
else:
    print(pickle.loads(pessoa).nome, 'é menor de idade')