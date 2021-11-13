num1 = int(input('Informe um número : '))
num2 = int(input('Informe outro número : '))

if(num1 > num2):
    print('O número {} é maior que {}'.format(num1,num2))
elif (num1 < num2):
    print('O número {} é maior que {}'.format(num2, num1))
else:
    print('Os número são iguais!')