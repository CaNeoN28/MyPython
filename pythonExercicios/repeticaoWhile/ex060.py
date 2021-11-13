prod = num = int(input('Informe um número : '))

msg = '{}! = '.format(num)
while num > 1:
    msg += '{} x '.format(num)
    num -= 1
    prod *= num

msg += '{} = {}'.format(num, prod)
print(msg)