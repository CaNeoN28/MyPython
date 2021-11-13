func = 4
while func != 5:
    if func == 4:
        num1 = int(input('Digite um número : '))
        num2 = int(input('Digite outro número : '))

    print(30 * '=')
    print('[1] Soma'
               '\n[2] Multiplicação'
               '\n[3] Maior'
               '\n[4] Digitar outros números'
               '\n[5] Sair do programa')
    print(30 * '=')
    func = int(input('Informe uma opção : '))
    if func == 1:
        print('A soma dos números {} e {} é {}'.format(num1, num2, num1+num2))
    elif func == 2:
        print('O produto dos números {} e {} é {}'.format(num1, num2, num1*num2))
    elif func == 3:
        msg = 'O número {} é maior que {}!'
        if num1 > num2:
            msg = msg.format(num1, num2)
        elif num2 > num1:
            msg = msg.format(num2, num1)
        else:
            msg = 'Os números são iguais!'
        print(msg)
    elif func != 5:
        print('Opção inválida!\nDigite novamente')

print('Tenha um bom dia!')