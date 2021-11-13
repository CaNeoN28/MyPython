adultos = homens = mul20 = cont = 0
while True:
    id = int(input('Informe a idade de uma pessoa : '))
    while True:
        sex = input('Informe o sexo dessa pessoa [M/F] : ')
        if sex in 'MmFf':
            break
        print('Sexo Inválido! Digite novamente')
    print(40 * '=')
    cont += 1
    if sex in 'Mm':
        homens += 1
    elif id < 20:
        mul20 += 1

    if id >= 18:
        adultos += 1

    opc = ''
    while True:
        opc = input('Deseja continuar [S/N]?')
        if opc in 'SsNn':
            break
        print('Opção Inválida! Digite novamente!')
    if opc in 'Nn':
        break
print(f'O número de registros foi de {cont} candidatos')
print(f'Entre eles há : \nHomens : {homens}\nAdultos : {adultos}\nMulheres com menos de 20 anos : {mul20}')
