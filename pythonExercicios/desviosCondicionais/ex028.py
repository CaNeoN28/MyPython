from random import randint

sort = randint(0, 5)
num = int(input('Digite um número de 0 a 5 : '))

if num <= 5:
    print('O número sorteado foi {}!'.format(sort))
    if num == sort:
        print('Parabéns! Você acertou!')
    else:
        print('Você errou, mais sorte na próxima!')
else:
    print('O número digitado é inválido!')
