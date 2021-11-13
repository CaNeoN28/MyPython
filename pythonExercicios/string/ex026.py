frase = input('Digite uma frase : ')
frase = frase.strip()
frase = frase.lower()

num = frase.count('a')

print('Existem {} letras "a" nessa frase'.format(num))
print('A primeira letra "a" está na posição : {}'.format(frase.find('a') + 1))
print('A última letra "a" está na posição : {}'.format(frase.rfind('a') + 1))
