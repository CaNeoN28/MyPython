lista = [[], []]

for c in range(0, 7):
    aux = int(input(f'Informe o {c + 1}° valor : '))
    res = aux % 2
    lista[res].append(aux)
    lista[res].sort()
print(f'Os números pares digitados são : {lista[0]}\n'
      f'Os números ímpares digitados são : {lista[1]}')