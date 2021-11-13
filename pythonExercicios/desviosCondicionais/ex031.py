dist = int(input('Informe a distância da viagem em Km : '))
valor = float()

if dist < 200 :
    valor = dist * 0.5
else:
    valor = dist * 0.45
print('O valor da viagem é de R${:.2f}'.format(valor))