tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Corinthias', 'Internacional', 'Athletico-PR',
          'Fluminense', 'América-MG', 'Atlético-GO', 'Cuiabá', 'Ceará SC', 'São Paulo', 'Juventude', 'Santos', 'Bahia',
          'Sport Recife', 'Grêmio', 'Chapecoense')
print(f'Os cinco primeiros colocados são : \n{tabela[0:5]}')
print(f'Os quatro ultimos colocados são : \n{tabela[len(tabela) - 4:len(tabela)]}')
print(f'A ordem alfabética dos times é : \n{sorted(tabela)}')
print(f'A Chapecoense se encontra na {tabela.index("Chapecoense") + 1}° posição da tabela')