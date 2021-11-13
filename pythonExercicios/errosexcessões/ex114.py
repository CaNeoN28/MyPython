import requests

try:
    response = requests.get('http://pudim.com.br')
except ConnectionError:
    print('\033[31mO sitem pudim não está acessível no momento!')
else:
    print('\033[36mO site pudim está acessível no momento!')