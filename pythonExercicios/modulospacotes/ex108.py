from modules import moeda
from modules import formatar

quant = float(input('Informe uma quantidade em dinheiro : R$'))
print(f'A metade desse valor é {formatar.moeda(moeda.metade(quant))}')
print(f'O dobro desse valor é {formatar.moeda(moeda.dobro(quant))}')
print(f'Com 8% de aumento, o valor passa a ser {formatar.moeda(moeda.aumentar(quant, 8))}')
print(f'Com 42% de redução, o valor passa a ser {formatar.moeda(moeda.diminuir(quant, 42))}')