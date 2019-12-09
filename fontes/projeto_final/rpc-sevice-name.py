# IMPORTANDO AS BIBLIOTECAS REQUERIDAS
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import pickle
import os.path
from threading import Lock, Semaphore
from threading import Thread
import time



# DECLARAÇÃO DE VARIÁVEIS
SERVICE_FILE = 'services.txt'
services = []



class ValidarServico(object):
    def __init__(self):
        pass

    def getProxy(self, url):
        with xmlrpc.client.ServerProxy(url) as proxy:
            return proxy

    def is_valid(self, servico):
        print(servico)
        url = 'http://' + str(servico['host']) + ':' + str(servico['port'])
        p = self.getProxy(url)
        try:
            valido = p.is_valid()
            if valido:
                print('is_valid: ' + str(url) + '- ' + str(servico['serviceName']) + str(valido))
                return True
        except Exception as e:
            print('is not valid: ' + str(url))
            return False


    def removeInactiveServices(self, services):
        for service in services:
            if not self.is_valid(service):
                print('serviço inválido: http://' + str(service['host']) + ':' + str(service['port']) + str(service['serviceName']))
                services.remove(service)
        f = open(SERVICE_FILE, "wb")
        f.write(pickle.dumps(services))
        f.close()



# FUNÇÃO PARA REGISTRAR UM NOVO SERVIÇO NO SERVIDOR DE NOMES
def serviceRegiste(serviceName, host, port):
    try:
        if not os.path.exists(SERVICE_FILE):
            print('file not exists')
            services = [{'serviceName':'0', 'host':'0', 'port':'0'}]
            f = open(SERVICE_FILE, "wb")
            f.write(pickle.dumps(services))
            f.close()
        f = open(SERVICE_FILE, "rb")
        services = pickle.loads(f.read())
        f.close()
        services.append({'serviceName':serviceName, 'host':host, 'port':port})
        f = open(SERVICE_FILE, "wb")
        f.write(pickle.dumps(services))
        f.close()
        return True
    except Exception as e:
        print('Erro ao registrar serviço ' + str(e))
        return False


# OBTER DADOS DE UM SERVIÇO (NOME, HOST E PORTA)
def listServices():
    try:
        f = open(SERVICE_FILE, "rb")
        services = pickle.loads(f.read())
        f.close()
        return services
    except Exception as e:
        print('Erro ao ler o arquivo de serviços !' + str(e))
        return pickle.dumps({'mess-error': e})

# FUNÇÃO PARA REMOVER O REGISTRO DE UM SERVIÇO NO SERVIDOR DE NOMES
def unregisteService(services):
    try:
        validator = ValidarServico()
        validator.removeInactiveServices(services)            
    except EOFError:
        print('Um erro ocorreu !')
#unregisteService(listServices())




# OBTER DADOS DE UM SERVIÇO (NOME, HOST E PORTA)
def getService(serviceName):
    listener()
    try:
        f = open(SERVICE_FILE, "rb")
        services = pickle.loads(f.read())
        f.close()
        for s in services:
            if s['serviceName'] == serviceName:
                return s
        return False
    except Exception as e:
        print('Erro na busca pelo serviço !' + str(e))
        return pickle.dumps({'mess-error': e})


class Worker(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        countServices = 1
        while countServices > 0:
            services = listServices()
            countServices = len(services)
            print('Cleaning services...')
            unregisteService(services)
            time.sleep(5)


def listener():            
    worker = Worker()
    worker.start()


# SUBIR O SERVIDOR E REGISTRAR SERVIÇOS
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening in port 8000 ...")
server.register_function(serviceRegiste, "serviceRegiste")
server.register_function(unregisteService, "unregisteService")
server.register_function(getService, "getService")
server.serve_forever()