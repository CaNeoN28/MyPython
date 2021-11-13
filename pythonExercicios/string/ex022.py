nome = input('Informe seu nome completo : ')
nome = nome.strip()
num = len(nome.replace(' ', ''))
primeiro = nome.split()[0]

print('Nome em maiúsculo : {}'.format(nome.upper()))
print('Nome em minusculo : {}'.format(nome.lower()))
print('Número de letras : {}'.format(num))
print('Numero de letras do primeiro nome : {}'.format(len(primeiro)))

