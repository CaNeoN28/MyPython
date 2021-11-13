def leiaInt(msg):
    num = 0
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print('\033[31mO valor digitado não é válido!')
            print('\033[m', end='')
        except KeyboardInterrupt:
            print('O usuário optou por não digitar o valor')
            break
    return num


def leiaFloat(msg):
    num = 0
    while True:
        try:
            num = float(input(msg))
            break
        except ValueError:
            print('\033[31mO valor digitado não é válido!')
            print('\033[m', end='')
        except KeyboardInterrupt:
            print('O usuário optou por não digitar o valor')
            break
    return num


n1 = leiaInt('Digite um número inteiro : ')
n2 = leiaFloat('Digite outro número : ')
print(f'Os valores digitados foram {n1} e {n2}')
