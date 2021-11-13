def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt:^{tam}}')
    print('~' * tam)


txt = input('Digite um texto qualquer : ')
escreva(txt)
