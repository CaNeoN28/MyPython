num = int(input('Informe o número a ser convertido: '))
opc = int(input('Digite 1 para binário\n'
                'Digite 2 para octal\n'
                'Digite 3 para hexadecimal\n'
                'Escolha uma base para conversão:'))
if(opc == 1):
    msg = format(num, 'b')
    print('O número em binário é : {}'.format(msg))
elif(opc == 2):
    msg = format(num, 'o')
    print('O número em octal é : {}'.format(msg))
elif(opc ==3):
    msg = format(num, 'x')
    print('O número em hexadecimal : {}'.format(msg))
else:
    print('Opção inválida!')
