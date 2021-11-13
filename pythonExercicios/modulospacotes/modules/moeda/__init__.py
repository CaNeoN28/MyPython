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


def moeda(a=0.0):
    moeda = f'R${a:.2f}'
    return moeda


def resumo(valor, aum=0, dim=0):
    print(30*'-')
    print(f'{"RESUMO DO VALOR":^30}')
    print(30*'-')

    print(f'{"Preço analisado ":<20}:{moeda(valor):>9}')
    print(f'{"Dobro do valor ":<20}:{dobro(valor,True):>9}')
    print(f'{"Metade do valor ":<20}:{metade(valor, True):>9}')
    msg = f'{aum}% de aumento '
    print(f'{msg:<20}:{aumentar(valor, aum, True):>9}')
    msg = f'{dim}% de aumento '
    print(f'{msg:<20}:{diminuir(valor, dim, True):>9}')
    print(30*'-')