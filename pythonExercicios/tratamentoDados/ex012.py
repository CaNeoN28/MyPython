preco = float(input('Informe o preço de um produto em reais: R$'))
desc = preco*5/100
preco = preco - desc

print('O novo preço do produto com 5% de desconto é de R${:.2f}'.format(preco))