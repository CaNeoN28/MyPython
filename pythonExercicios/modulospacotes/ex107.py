from modules import moeda

quant = float(input('Informe uma quantia em dinheiro : R$'))
print(f'O dobro de {quant} é {moeda.dobro(quant)}')
print(f'A metade de {quant} é {moeda.metade(quant)}')
print(f'Com 15% de aumento, o valor passa a ser de {moeda.aumentar(quant, 15)}')
print(f'Com 8% de redução, o valor passa a ser de {moeda.diminuir(quant, 8)}')