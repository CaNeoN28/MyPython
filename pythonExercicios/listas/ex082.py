lista = []
par = []
impar = []
while True:
    lista.append(int(input('Informe um número : ')))
    opc = ''
    while True:
        opc = input('Deseja continuar? [S/N]\n')[0]
        if opc in 'SsNn':
            break
        else:
            print('Opção inválida! Digite novamente!')
    if opc in 'Nn':
        break
    print('Vamos continuar!')
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('Os números digitados foram : ')
for c in lista:
    print(c, end = ' ')
print('\nOs números pares digitados foram : ')
for c in par:
    print(c, end=' ')
print('\nOs números impares digitados foram : ')
for c in impar:
    print(c, end=' ')