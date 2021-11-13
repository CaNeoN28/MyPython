from modulospacotes.ex112.utilidadesCeV import dado


def aumentar(a, b=0, c=False):
    aum = float(b/100) * a
    valor = a + aum
    if c:
        return f'R${valor:.2f}'
    return valor


def diminuir(a, b=0, c=False):
    dim = float(b/100) * a
    valor = a - dim
    if c:
        return f'R${valor:.2f}'
    return valor


def dobro(a, b=False):
    valor = 2*a
    if b:
        return f'R${valor:.2f}'
    return valor

def metade(a, b=False):
    valor = a/2
    if b:
        return f'R${valor:.2f}'
    return valor


def moeda(a):
    msg = f'R${a:.2f}'
    return msg


def resumo(valor, aum=0, dim=0):
    print(30*'-')
    print(f'{"RESUMO DO VALOR":^30}')
    print(30*'-')

    valores = []
    aux = valor
    aux = float(aux.replace(',', '.'))

    valores.append(moeda(aux))
    valores.append(dobro(aux, True))
    valores.append(metade(aux, True))
    valores.append(aumentar(aux, aum, True))
    valores.append(diminuir(aux, dim, True))

    if ',' in valor:
        for c in range(0, len(valores)):
            valores[c] = valores[c].replace('.', ',')

    print(f'{"Preço analisado ":<20}:{valores[0]:>9}')
    print(f'{"Dobro do valor ":<20}:{valores[1]:>9}')
    print(f'{"Metade do valor ":<20}:{valores[2]:>9}')
    msg = f'{aum}% de aumento '
    print(f'{msg:<20}:{valores[3]:>9}')
    msg = f'{dim}% de aumento '
    print(f'{msg:<20}:{valores[4]:>9}')
    print(30*'-')