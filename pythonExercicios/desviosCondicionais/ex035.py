lado1 = int(input('Informe a medida de tamanho de uma reta : '))
lado2 = int(input('Informe a medida de tamanho de outra reta : '))
lado3 = int(input('Informe a medida de tamanho de mais uma reta : '))

if lado1 + lado2 >= lado3 and lado1 + lado3 >= lado2 and lado1 + lado3 >= lado2:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo!')
