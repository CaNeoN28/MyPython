frase = input('Digite uma frase : ').strip()
aux = frase.lower().replace(' ','')
comp = len(aux)
esarf = ''

for c in range(0, comp):
    esarf += aux[comp - c - 1]

if aux == esarf:
    print('A frase "{}" é um palíndromo!'.format(frase))
else:
    print('A frase "{}" não é um palíndromo!'.format(frase))
