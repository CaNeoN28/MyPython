menorV = valor = prod1000 = cont = 0
menorN = ''
while True:
    nome = input('Informe o nome do produto : ')
    aux = float(input('Informe o preço do produto : R$'))
    valor += aux
    opc = ''

    if aux > 1000:
        prod1000 += 1

    if cont == 0 or menorV > aux:
        menorN = nome
        menorV = aux

    while True:
        opc = input('Mais alguma coisa [S/N]? ')
        if opc in 'SsNn':
            break
        print('Opção Inválida! Digite novamente')
    if opc in 'Nn':
        break
print(f'O valor total das compras foi : {valor:.2f}\n'
      f'O número de produtos com preço superior a R$1000 é de : {prod1000}\n'
      f'O nome do produto mais barato é {menorN} e seu valor é de R${menorV:.2f}')