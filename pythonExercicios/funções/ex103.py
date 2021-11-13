def ficha(nome='<desconhecido>', gols = 0):
    return(f'O jogador {nome} fez {gols} gol(s) no campeonato!')


nome = str(input('Informe o nome de um jogador : '))
gols = str(input('Informe o total de gols desse jogador : '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    print(ficha(gols = gols))
else:
    print(ficha(nome, gols))
