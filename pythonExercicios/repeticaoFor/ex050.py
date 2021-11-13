sum = 0
for c in range(0, 6):
    num = int(input('Informe um número : '))
    if num % 2 == 0:
        sum += num
print('A soma dos números pares é : {}'.format(sum))