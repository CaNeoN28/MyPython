num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

opc = 0
while True:
    opc = int(input('Digite um número de 0 a 20 : '))
    if 0 <= opc <= 20:
        break
    print('Número Inválido!', end = ' ')

print(f'Você escolheu o número {num[opc]}!')