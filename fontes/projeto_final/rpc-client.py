import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print('....................................')
    print('3 é par: %s' % str(proxy.is_even(3)))
    print('....................................')
    print('....................................')
    print(proxy.getService('sqrtd'))
    print('....................................')