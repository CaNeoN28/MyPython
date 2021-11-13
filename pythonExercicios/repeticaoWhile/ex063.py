n = int(input('Informe um termo : '))
ant = 0
num = 1
msg = 'Os números da sequência de Fibbonacci até o {}° termo é :\n'.format(n)

while n > 1:
    msg += '{} → '.format(ant)
    aux = num
    num += ant
    ant = aux
    n -= 1

msg += '{}'.format(ant)
print(msg)
