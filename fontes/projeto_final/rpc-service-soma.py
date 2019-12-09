import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer


# DEFININDO UM SERVIÇO
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def prod(a, b):
    return a * b

def div(a, b):
    return a / b

def is_valid():
    return True


# PUBLICANDO SERVIÇOS NO SERVIDOR DE NOMES
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print('....................................')
    print('Registrando serviço de soma')
    proxy.serviceRegiste('soma', 'localhost', '8001')
    print('Registrando serviço prod')
    proxy.serviceRegiste('prod', 'localhost', '8001')
    print('Registrando serviço sub')
    proxy.serviceRegiste('sub', 'localhost', '8001')
    print('Registrando serviço div')
    proxy.serviceRegiste('div', 'localhost', '8001')
    #proxy.unregisteService('192.168.1.100')


# SUBINDO O SERVIDOR E REGISTRANDO O SERVIÇO
server = SimpleXMLRPCServer(("localhost", 8001))
print("Listening in port 8001 ...")
server.register_function(soma, "soma")
server.register_function(sub, "sub")
server.register_function(prod, "prod")
server.register_function(div, "div")
server.register_function(is_valid, 'is_valid')
server.serve_forever()