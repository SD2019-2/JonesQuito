# Importa os objetos necessários para o funcionamento do cliente
import socket
import pickle
from utils import ClienteSocket

# Declara um vetor de notas
notas = []

# Recuperar entrada do usuário
notas.append(float(input("Informe a nota 1: ")))
notas.append(float(input("Informe a nota 2: ")))
notas.append(float(input("Informe a nota 3: ")))

# Prepara os dados para envio
dados = {'op': 'media', 'dados':notas}
dados = pickle.dumps(dados)

# Instancia um cliente socket e envia os dados
cliente = ClienteSocket('localhost', 3000)
cliente.enviar(dados)

# Receber o resultado e imprimir
media = pickle.loads(cliente.recebe())
print("Média: ", media)


