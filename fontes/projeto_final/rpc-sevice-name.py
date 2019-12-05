# IMPORTANDO AS BIBLIOTECAS REQUERIDAS
from xmlrpc.server import SimpleXMLRPCServer
import pickle
import os.path



# DECLARAÇÃO DE VARIÁVEIS
SERVICE_FILE = 'services.txt'
services = []



# FUNÇÃO PARA REGISTRAR UM NOVO SERVIÇO NO SERVIDOR DE NOMES
def serviceRegiste(serviceName, host, port):
    try:
        f = open(SERVICE_FILE, "rb")
        services = pickle.loads(f.read())
        f.close()
        services.append({'serviceName':serviceName, 'host':host, 'port':port})
        f = open(SERVICE_FILE, "wb")
        f.write(pickle.dumps(services))
        f.close()
    except Exception:
        print('Erro ao registrar serviço')
#serviceRegiste('sqrt', 'localhost', 1234)



# FUNÇÃO PARA REMOVER O REGISTRO DE UM SERVIÇO NO SERVIDOR DE NOMES
def unregisteService(host):
    try:
        f = open(SERVICE_FILE, "rb")
        services = pickle.loads(f.read())
        f.close()
        for item in services:
            print(item)
            if item['host']==host:
                services.remove(item)
                f = open(SERVICE_FILE, "wb")
                f.write(pickle.dumps(services))
                f.close()
    except EOFError:
        print('Um erro ocorreu !')
#unregisteService('localhost')




# OBTER DADOS DE UM SERVIÇO (NOME, HOST E PORTA)
def getService(serviceName):
    try:
        f = open(SERVICE_FILE, "rb")
        services = pickle.loads(f.read())
        f.close()
        for s in services:
            if s['serviceName'] == serviceName:
                return s
        return False
    except Exception:
        print('Erro na busca pelo serviço !')
#print(getService('sqrt'))



# FUNÇÃO DE TESTE
def is_even(n):
    print("Requisição recebida com o seguinte argumento " + str(n))
    return n % 2 == 0



# SUBIR O SERVIDOR E REGISTRAR SERVIÇOS
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening in port 8000 ...")
server.register_function(is_even, "is_even")
server.register_function(serviceRegiste, "serviceRegiste")
server.register_function(unregisteService, "unregisteService")
server.register_function(getService, "getService")
server.serve_forever()