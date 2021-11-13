num = []

for c in range(1, 6):
    num.append(int(input(f'Informe o {c}° número da lista : ')))

maior = max(num)
posmax = ''
menor = min(num)
posmin = ''

for c in range(0, len(num)):
    if maior == num[c]:
        posmax += f'{c}.. '
for c in range(0, len(num)):
    if menor == num[c]:
        posmin += f'{c}...'

if len(posmax.split()) > 1:
    print(f'O maior número é {maior} e ele foi encontrado nas posições : {posmax}')
else:
    print(f'O maior número é {maior} e ele foi encontrado na posição : {posmax}')

if len(posmin.split()) > 1:
    print(f'O menor número é {menor} e ele foi encontrado nas posições : {posmin}')
else:
    print(f'O menor número é {menor} e ele foi encontrado na posição : {posmin}')