num = int(input('Informe um número : '))
res = 0

for c in range(1, num):
    if num % c == 0:
        res += 1
if res > 1:
    print('O número {} não é primo!'.format(num))
else:
    print('O número {} é primo!'.format(num))
