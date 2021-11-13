from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os números sorteados foram : ', end='')
for c in num:
    print(c, end=' ')

num = sorted(num)
print(f'\nO menor e o maior número são {num[0]} e {num[len(num) - 1]}, respectivamente')
