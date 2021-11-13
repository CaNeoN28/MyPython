from random import randint
from time import sleep
from operator import itemgetter

jogador = {'nome':'', 'dado':0}
jogadores = []

for a in range(1,5):
    jogador['nome'] = f'número {a}'
    jogador['dado'] = randint(1,6)
    jogadores.append(jogador.copy())
    print(f'O jogador {jogador["nome"]} tirou {jogador["dado"]} nos dados!')
    sleep(0.5)

ordem = sorted(jogadores, key=itemgetter('dado'), reverse=True)
'''dados = []
ordem = []
for a in jogadores:
    dados.append(a['dado'])

dados.sort(reverse=True)'''

'''for a in range(0, 4):
    for b in jogadores:
        if b['dado'] == dados[a] and b not in ordem:
            ordem.append(b.copy())'''

print(10 * '=', ' LISTA DE JOGADORES ', '=' * 10)
print(f'{"POS":<5}', f'{"NOME":<10}', f'{"DADO":>5}')
for c in ordem:
    print(f'{ordem.index(c) + 1}{"º":<4}', f'{c["nome"]:<10}', f'{c["dado"]:>5}')
    sleep(0.5)