somap = 0
soma3 = 0
maior2 = 0
lista = list()
for c in range (0, 3):
    lista.append([])

for a in lista:
    for b in range(0, 3):
        n = lista.index(a)
        aux = int(input(f'Informe um número para a posição [{n}:{b}] : '))
        a.append(aux)
        if aux % 2 == 0:
            somap += aux
        if b == 2:
            soma3 += aux
        if n == 1:
            if b == 0:
                maior2 = aux
            elif maior2 < aux:
                maior2 = aux

print(40 * '-')
for a in lista:
    for b in range(0, 3):
        print(f'[{a[b]:^5}]', end=' ')
    print('')
print(40 * '-')

print(f'A soma dos números pares é : {somap}\n'
      f'A soma dos números da 3ª coluna é : {soma3}\n'
      f'O maior número da 2ª fileira é : {maior2}')
