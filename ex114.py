import requests

try:
    res = requests.get('http://www.pudim.com.br')
except requests.exceptions.ConnectionError:
    print('Site indisponivel.')
else:
    print('Site disponivel.')
