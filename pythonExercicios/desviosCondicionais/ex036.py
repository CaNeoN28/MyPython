casa = float(input('Informe o valor da casa : '))
sal = float(input('Informe o seu salário : '))
temp = int(input('Informe o tempo que deseja levar para pagar em anos: '))

mens = casa/temp/12
print('Prestação : R${}\n'
      'Mínimo : R${}'.format(mens, sal*0.3))
if(mens <= sal * 0.3):
    print('Empréstimo concedido!')
else:
    print('Infelizmente o empréstimo não pode ser concedido!')