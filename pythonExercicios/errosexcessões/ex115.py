from ex115 import Titulo, Cadastrar, Listar
from time import sleep

opc = ['Cadastrar uma pessoa',
       'Verificar a lista',
       'Sair do programa']

while True:
    Titulo('MENU PRINCIPAL')
    for c in opc:
        print (f'{opc.index(c) + 1} - {c}')
    print('~~' * 30)
    try:
        aux = opc[int(input('Informe sua opção: '))-1]
        if opc.index(aux) == 0:
            Cadastrar()
        elif opc.index(aux) == 1:
            Listar()
        elif opc.index(aux) == 2:
            sleep(1)
            break
    except ValueError:
        print('\033[31mERRO : O valor informado não é válido!\033[m')
    except IndexError:
        print('\033[31mERRO : Opção inválida!\033[m')

print('Tenha um bom dia!')
