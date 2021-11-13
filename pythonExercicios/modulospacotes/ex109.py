from modules import moeda
from modules import formatar

quant = float(input('Informe uma quantidade em dinheiro : R$'))
print(f'A metade desse valor é {moeda.metade(quant, True)}')
print(f'O dobro desse valor é {moeda.dobro(quant)}')
print(f'Com 28% de aumento, o valor passa a ser {moeda.aumentar(quant, 28, True)}')
print(f'Com 17% de redução, o valor passa a ser {moeda.diminuir(quant, 17)}')