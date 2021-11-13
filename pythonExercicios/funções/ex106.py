c = ('\033[m',
     '\033[36m',
     '\033[33m',
     '\033[34m')


def titulo(msg, cor = 0):
    print(c[cor])
    print('~' * (len(msg) + 4))
    print(f'{msg:^{len(msg) + 4}}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')

def ajuda(opc, cor = 0):
    titulo(f'Ajuda para a biblioteca \'{opc}\'', 2)
    print(c[cor])
    help(opc)

while True:
    titulo("Biblioteca de ajuda Python", 1)
    opc = input('Informe uma funcao (fim para) -> ').lower()
    if opc == 'fim':
        break
    ajuda(opc, 3)