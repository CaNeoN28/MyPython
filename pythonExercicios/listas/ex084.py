pessoas = list()
maior = menor = 0
while True:
    pessoa = list()
    pessoa.append(input('Informe o nome de uma pessoa : '))
    pessoa.append(float(input('Informe o peso dessa pessoa em Kg : ')))
    pessoas.append(pessoa[:])

    if len(pessoas) == 1:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if maior < pessoa[1]:
            maior = pessoa[1]
        if menor > pessoa[1]:
            menor = pessoa[1]
    opc = ''
    while True:
        opc = input('Deseja continuar? [S/N] ')[0]
        if opc in 'SsNn':
            break
        else:
            print('Opção inválida! Digite novamente')
    if opc in 'Nn':
        break
    print('Vamos continuar!')

num = len(pessoas)
print(f'Você informou o dado de {num} pessoas')
peso = list()
for c in pessoas:
    if c[1] == maior:
        peso.append(c[0])
print(f'O maior peso registrado foi de {maior}Kg, pertencendo a {peso}')
peso.clear()
for c in pessoas:
    if c[1] == menor:
        peso.append(c[0])
print(f'O menor peso registrado foi de {menor}Kg, pertencendo a {peso}')
