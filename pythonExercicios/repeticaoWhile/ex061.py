term1 = int(input('Informe o primeiro termo da PA : '))
raz = int(input('Informe a razão dessa PA : '))

term = 1

msg = 'Os dez primeiros termos da PA são : \n{} '.format(term1)

while term < 10:
    term += 1
    prod = term1 + (term - 1) * raz
    msg += '{} '.format(prod)

print(msg)