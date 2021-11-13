preco = float(input('Informe o preço do produto: R$'))
met = int(input('''1 - A vista (Dinheiro)
2 - A vista (Cartão)
3 - Parcelado 2x no cartão
4 - Parcelado 3 ou mais vezes no cartão
Informe o método de pagamento : '''))
msg = ''
if met == 1:
    preco = preco * 0.9
    msg = 'com 10% de desconto'
elif met == 2:
    preco = preco * 0.95
    msg = 'com 5% de desconto'
elif met == 3:
    msg = ''
elif met == 4:
    preco = preco * 1.2
    msg = 'com 20% de juros'
else:
    print('Opção inválida!')
    exit()

print('O preço do produto ficou R${} {}'.format(preco, msg))
