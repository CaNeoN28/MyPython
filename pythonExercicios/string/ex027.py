nome = input('Informe seu nome completo : ')
nome = nome.strip()
primeiro = nome.split()[0]
ultimo = nome.split()[len(nome.split()) - 1]

print('Primeiro nome : {}'.format(primeiro))
print('Ultimo nome : {}'.format(ultimo))