sal = float(input('Informe o salário de funcionário : '))

if sal <= 1250.00:
    sal = sal * 1.15
else:
    sal = sal * 1.10
print('O novo salário do funcionário é de : {:.2f}R$'.format(sal))