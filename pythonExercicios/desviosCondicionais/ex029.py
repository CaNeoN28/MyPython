vel = float(input('Digite sua velocidade em km/h : '))

if vel > 80:
    print('Você foi multado! Você ultrapassou o limite de 80Km/h!')
    multa = (vel - 80) * 7
    print('O valor da multa é de : {:.2f}R$'.format(multa))
else:
    print('Você está dentro do limite de 80Km/h, continue assim!')