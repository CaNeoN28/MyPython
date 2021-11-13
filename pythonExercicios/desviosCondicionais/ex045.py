from random import randint
from time import sleep

opc = ['pedra', 'papel', 'tesoura']
user = int(input('1 - Pedra\n'
                '2 - Papel\n'
                '3 - Tesoura\n'
                'Escolha uma opção : '))

if user > len(opc):
    print('Opção Inválida!')
    exit()

print('Pedra!')
sleep(1)
print('Papel!')
sleep(1)
print('Tesoura!')
sleep(1)

user = opc[user - 1]

print('Você escolheu {}!'.format(user))

maq = opc[randint(0, 2)]

if maq == user :
    print('Foi um impate!')
elif user == 'pedra' and maq == 'papel' or user == 'papel' and maq == 'tesoura' or user == 'tesoura' and maq == 'pedra':
    print('A máquina escolheu {}!\nVocê perdeu!'.format(maq))
else:
    print('A máquina escolheu {}!\nVocê ganhou!'.format(maq))


