num = int(input('Informe um número : '))
raz = int(input('Informe a razão da progressão : '))

for c in range(1,11):
    res = num + (c-1) * raz
    print('{}° termo da progressão aritmética : {}'.format(c, res))
