palavras = ('hamburguer', 'livro', 'jogo', 'feliz', 'diversao')

for a in palavras:
    a = a.upper()
    print(f'Na palavra {a} temos as vogais : ', end='')
    for b in a:
        if b in 'AEIOU':
            print(b, end=' ')
    print('')
