lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for c in lanche:
    print(c)

for pos, c in enumerate(lanche):
    print(f'Vou comer o lanche {c} na posição {pos}!')

for c in range(0, len(lanche)):
    print(f'Vou comer o lanche {lanche[c]} na posição {c}')

del(lanche)