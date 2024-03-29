import socket
import pickle

from models import Pessoa
from utils import ClienteSocket


# Prepara os dados para envio
pessoa = Pessoa('Jones', 17, 'm')
dados = {'op': 'maioridade', 'dados':pessoa}
dados = pickle.dumps(dados)

# Instancia um cliente socket e envia os dados
cliente = ClienteSocket('129.213.164.45', 3000) #129.213.164.45
cliente.enviar(dados)


resposta = pickle.loads(cliente.recebe())
if resposta:
    print('É maior de idade')
else:
    print('É menor de idade')
