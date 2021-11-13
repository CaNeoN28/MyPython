term1 = int(input('Informe o primeiro termo da PA : '))
raz = int(input('Informe a razão dessa PA : '))

term = 1

msg = 'Os {} primeiros termos da PA são : \n{} '.format(10, term1)

while term < 10:
    term += 1
    prod = term1 + (term - 1) * raz
    msg += '{} '.format(prod)

print(msg)

aux = 1
while aux != 0:
    aux = int(input('Quantos termos extras você deseja? ')) + 1
    term += aux - 1
    msg = 'Os {} termos extras são :\n'.format(aux - 1)
    while aux > 1:
        prod += raz
        msg += '{} '.format(prod)
        aux -= 1
    if aux > 0 :
        print(msg)

print('O número total de termos foi de {} termos'.format(term))
print('Tenha um bom dia')