jogador = {}
jogador['nome'] = input('Informe o nome de um jogador : ')
jogador['jogos'] = int(input('Quantos jogos esse jogador participou? '))
jogador['gols'] = []

print(30 * '-=')

for c in range(1, jogador['jogos'] + 1):
    jogador['gols'].append(int(input(f'Quantos gols fez {jogador["nome"]} no {c}° jogo? ')))

jogador['total'] = sum(jogador['gols'])

print('-=' * 30)

print(f'O jogador {jogador["nome"]} participou de {jogador["jogos"]} jogos')
for c, v in enumerate(jogador["gols"]):
    print(f'No {c + 1}° jogo, {jogador["nome"]} fez {v} gols')
print(f'Ao todo, {jogador["nome"]} fez {jogador["total"]} gols')
