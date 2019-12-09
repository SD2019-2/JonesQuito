import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

    somaService = proxy.getService('soma')
    print(somaService)
    url = 'http://' + str(somaService['host']) + ':' + str(somaService['port'])
    print(url)
    with xmlrpc.client.ServerProxy(url) as proxy2:
        try:
            print(proxy2.soma(2, 8))
            print(proxy2.prod(2, 8))
            print(proxy2.div(8, 2))
        except Exception as e:
            print('Serviço indisponível !!' , e)
    

    