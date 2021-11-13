list = []
for c in range(0, 5):
    cond = True
    aux = int(input(f'Informe o {c + 1}° valor : '))
    for a in range(0, len(list)):
        if aux <= list[a]:
            pos = a
            cond = False
            list.insert(a, aux)
            break
    if cond:
        list.append(aux)

print('Os valores digitados foram : ')
for c in list:
    print(c, end=' ')