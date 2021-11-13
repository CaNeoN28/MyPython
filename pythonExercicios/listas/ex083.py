exp = input('Informe uma expressão com parênteses : ')
lista = []

for c in exp:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) > 0:
    print('A expressão é inválida!')
else:
    print('A expressão é válida!')
