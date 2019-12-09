

class ValidarServico(object):
    def __init__(self):
        pass

    def getProxy(self, url):
        with xmlrpc.client.ServerProxy(url) as proxy:
            return proxy

    def is_valid(self, servico):
        #[{'serviceName':'0', 'host':'0', 'port':'0'}]
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
        f = open(self.SERVICE_FILE, "wb")
        f.write(pickle.dumps(services))
        f.close()
