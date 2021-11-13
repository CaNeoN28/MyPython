lista = [[],[],[]]

for a in lista:
    for b in range(0, 3):
        a.append(int(input(f'Informe um número para a posição [{lista.index(a)}:{b}] : ')))

print(40 * '-')
for a in lista:
    for b in range(0, 3):
        print(f'[{a[b]:^5}]', end=' ')
    print('')

