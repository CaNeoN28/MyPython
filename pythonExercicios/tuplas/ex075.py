num = (int(input('Digite um número')),
       int(input('Digite outro número : ')),
       int(input('Digite mais um número : ')),
       int(input('Digite um último número : ')))

c9 = 0
par = ''
c3 = 0

if 3 in num:
    c3 = num.index(3) + 1

for c in num:
    if c == 9:
        c9 += 1
    if c % 2 == 0:
        par += f'{c} '

if c9 == 0:
    print('O número 9 não aparece nenhuma vez')
else:
    print(f'O número 9 aparece {c9} vez(es)')
if c3 == 0:
    print('O número 3 não aparece')
else:
    print(f'O número 3 aparece não {c3}ª posição')
if par == '':
    print('Não há números pares')
else:
    print(f'Os números pares são : {par}')