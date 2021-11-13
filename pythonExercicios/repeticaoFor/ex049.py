num = int(input('Informe um número : '))

print('{:=^20}'.format('TABUADA'))
for c in range(1,11):
    print('{} x {: ^3} = {: ^3}'.format(num, c, num*c))
print('=' * 20)