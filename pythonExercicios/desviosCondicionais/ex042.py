lado1 = int(input('Informe a medida do 1° lado de um triângulo : '))
lado2 = int(input('Informe a medida do 2° lado de um triângulo : '))
lado3 = int(input('Informe a medida do 3° lado de um triângulo : '))
msg = ''

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    if lado1 == lado2 == lado3:
        msg = 'EQUILÁTERO'
    elif lado1 != lado2 and lado3 != lado1 and lado3 != lado2:
        msg = 'ESCALENO'
    else:
        msg = 'ISÓSCELES'
    print('O triângulo formado é : {}'.format(msg))
else:
    print('Não pode ser formado um triângulo!')
