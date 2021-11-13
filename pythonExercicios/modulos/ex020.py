from random import shuffle

nome1 = input('Informe o nome do primeiro aluno : ')
nome2 = input('Informe o nome do segundo aluno : ')
nome3 = input('Informe o nome do terceiro aluno : ')
nome4 = input('Informe o nome do quarto aluno : ')
lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print('A ordem de apresentação é : \n{}'.format(lista))
