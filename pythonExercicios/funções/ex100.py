from random import randint
from time import sleep


def sort(lst, b):
    for c in range(0, b):
        aux = 0
        while True:
            aux = randint(1, 100)
            if aux not in lst:
                break
        lst.append(aux)
    return lst


def somaP(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    return soma


lst = []
sort(lst, 8)
print('Os números sorteados foram : ')
for c in lst:
    sleep(0.5)
    print(c, end=' ')
print('')
sleep(1)
soma = somaP(lst)
print(f'A soma dos números pares sorteados é de : {soma}')