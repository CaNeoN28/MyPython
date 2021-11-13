from math import trunc

num = float(input('Informe um número real : '))
inteiro = int(trunc(num))

print('A parte inteira de {} é {}'.format(num, inteiro))