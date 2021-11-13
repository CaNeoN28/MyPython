num = []

while True:
    opc = ''
    aux = int(input('Digite um número : '))
    if aux not in num:
        print('Número já registrado! Tente novamente!')
    else:
        num.append(aux)
        while True:
            opc = input('Deseja continuar [S/N]?')
            if opc in 'SsNn':
                break
            else:
                print('Opção Inválida! Digite novamente!')
    if opc in 'Ss':
        print('Então vamos continuar!')
    elif opc in 'Nn':
        break

num.sort()
print('Os números digitados em ordem cresecente são : ')
for c in num:
    print(c, end=' ')