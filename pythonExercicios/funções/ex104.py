def leiaInt(str):
    while True:
        num = input(str)
        if num.isnumeric():
            return int(num)
        print('\033[31mValor Inválido!\033[m')


n = leiaInt('Digite um número : ')
print(f'Você digitou o número {n}')