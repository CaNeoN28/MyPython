def fatorial(num, show=False):
    '''
    Retorna o resultado do fatorial de um número
    :param num: Número inteiro a receber um fatorial
    :param show: Se verdadeiro, retorna os passos do fatorial (Opcional)
    :return: Sequência da fatoração
    '''

    msg = f'{num}! = '
    res = 1
    for c in range(num, 0, -1):
        res *= c
        if show:
            if c == 1:
                msg += f'{c} = '
            else:
                msg += f'{c} * '
    msg += f'{res}'
    return msg


f1 = fatorial(7)
f2 = fatorial(5, True)

print(f1)
print(f2)