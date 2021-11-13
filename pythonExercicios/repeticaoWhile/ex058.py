from random import randint

comp = randint(1, 10)
cond = True
ten = 0

while cond:
    ten += 1
    user = int(input('Informe um número de 1 a 10: '))

    if 1 <= user <= 10:
        if user == comp:
            cond = False
            print('Você ganhou!')
        else:
            print('Você errou!\nTente novamente')
    else:
        print('Número inválido!')
        ten -= 1

print('Você precisou de {} tentativas!'.format(ten))
