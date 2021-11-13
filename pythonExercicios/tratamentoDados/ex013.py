sal = float(input('Informe o salário de um funcionário : R$'))
aum = 15
sal = sal + (sal*aum/100)

print('O novo salário do funcionário com {}% de aumento é de R${:.2f}'.format(aum, sal))
