tempo = int(input('Informe o tempo em dias do aluguel do carro : '))
dist = float(input('Informe a distância em quilômetros que o carro percorreu : '))

aluguel = tempo * 60 + dist * 0.15

print('O valor total do aluguel é de R${:.2f}'.format(aluguel))