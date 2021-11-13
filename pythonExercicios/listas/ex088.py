from random import randint
from time import sleep

j = int(input('Quantos jogos você deseja fazer ? '))
num = list()

for a in range(0, j):
    num.append([])
    for b in range(0, 6):
        aux = randint(1, 60)
        while aux in num[a]:
            aux = randint(1, 60)
        num[a].append(aux)
    num[a].sort()

print(30 * '-=')

for c in num:
    n = num.index(c)
    print(f'Resultado do {n + 1}° jogo : {c}')
    sleep(0.5)

print(30 * '=-')