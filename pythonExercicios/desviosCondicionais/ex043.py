peso = float(input('Informe seu peso em Kg : '))
alt = float(input('Informe sua altura em cm : ')) / 100
imc = peso/alt**2
msg = ''

if imc < 18.5:
    msg = 'abaixo do peso'
elif imc < 25:
    msg = 'com peso ideal'
elif imc < 30:
    msg = 'acima do peso'
elif imc < 40:
    msg = 'com obesidade'
else:
    msg = 'com obesidade mórbida'

print('Com IMC de {:.2f} você está {}'.format(imc,msg))
