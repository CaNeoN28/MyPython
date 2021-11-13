list = []

while True:
    list.append(int(input('Digite um número : ')))
    opc = ''
    while True:
        opc = input('Deseja continuar ?[S/N] ')[0]
        if opc in 'SsNn':
            break
        else:
            print('Opção Inválida! Digite novamente')
    if opc in 'Nn':
        break
    print('Então vamos continuar!')

list.sort(reverse=True)
num = len(list)
print(f'A quantidade de números digitados é de : {num}\n'
      'Esses números em ordem decrescente são : ')
for c in list:
    print(c, end=' ')
print(f'\nDentre estes {num} números ', end='')
if 5 in list:
    print('há o número Cinco')
else:
    print('não há o número Cinco')