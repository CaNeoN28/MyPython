from time import sleep

def cont(i, f, p):
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p:}')
    if f > i:
        f += 1
        if p < 0:
            p = -p
    elif f < i:
        f -= 1
        if p > 0:
            p = -p
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(1)
    print('')
    print(40 * '~')


cont(1, 10, 1)
cont(10, 0, 2)
i = int(input('Informe o número inicial da contagem : '))
f = int(input('Informe o número final da contagem : '))
p = int(input('Informe o número de passos : '))
cont(i, f, p)