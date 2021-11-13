jogadores = []
jogador = {}

while True:
    jogador['nome'] = input(f'Informe o nome {len(jogadores) + 1}° jogador : ')
    c = jogador['jogos'] = int(input('De quantos jogos participou esse jogador? '))
    jogador['gols'] = []
    jogador['total'] = 0
    for a in range(0, c):
        jogador['gols'].append(int(input(f'Quantos gols fez esse jogador em sua {a + 1}ª partida? ')))
        jogador['total'] += jogador['gols'][a]
    jogadores.append(jogador.copy())
    opc = ''
    while True:
        opc = input('Deseja cadastrar mais algum jogador? [S/N] ')[0]
        if opc in 'SsNn':
            break
        print('Opção inválida!')
    if opc in 'Nn':
        break
    print('=' * 50)
    print('Vamos continuar!')

print('-' * 50)
print(f'{"JOGADORES":^50}')
print(50 * '-')
print(f'{"ID":>2}', f'{"NOME":<21}', f'{"GOLS":<21}', f'{"TOTAL":<5}')

for c in jogadores:
    print(f'{jogadores.index(c):>2}', f'{c["nome"]:<22}', end='')
    msg = ''
    for a in c['gols']:
        msg += f'{a} '
    msg.strip()
    print(f'{msg:<21}', f'{c["total"]}')
print(50 * '-')
while True:
    opc = int(input('Você deseja fazer o levantamento de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    elif opc < len(jogadores):
        print('-' * 50)
        jogador = jogadores[opc].copy()
        print(f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} jogos')
        for c, v in enumerate(jogador["gols"]):
            print(f'No {c + 1}° jogo, ele fez {v} gols')
        print(f'Ao todo, ele fez {jogador["total"]} gols')
        print('-' * 50)
    else:
        print('Jogador não disponível!')