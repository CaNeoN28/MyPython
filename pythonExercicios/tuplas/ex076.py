lista = ('Lápis', 1.75,  'Borracha', 2,  'Caderno', 15.9,  'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print(40 * '-')
print(f'{"Papelaria São José":^40}')
print(40 * '-')

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<32}', end='')
    else:
        print(f'R${lista[c]:>7.2f}')