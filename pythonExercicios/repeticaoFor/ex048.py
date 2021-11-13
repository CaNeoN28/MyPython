sum = 0
for c in range(3, 501, 3):
    if  c % 2 == 1:
        sum += c
print('Soma dos números múltiplos de 3 entre 1 e 500 : {}'.format(sum))