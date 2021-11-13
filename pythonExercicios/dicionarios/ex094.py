pessoas = []
pessoa = {}
while True:
    opc = ''
    pessoa['nome'] = input(f'Informe o nome da {len(pessoas) + 1}ª pessoa : ')
    while True:
        pessoa['sexo'] = input('Informe o sexo dessa pessoa : [M/F] ')[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('Sexo Inválido!')
    pessoa['idade'] = int(input('Informe a idade dessa pessoa : '))
    pessoas.append(pessoa.copy())
    while True:
        opc = input('Deseja continuar? [S/N] ')[0]
        if opc in 'SsNn':
            print('=' * 40)
            break
        print('Opção Inválida!')
    if opc in 'Nn':
        break
    print('Vamos continuar!')

print('=' * 40)

max = len(pessoas)
media = 0.0
for c in pessoas:
    if 'media' not in c.keys():
        media += c['idade']
media /= max
print(f'Ao todo, {max} pessoas foram registradas\n'
      f'A média das idades é de {media} anos\n')
mulheres = []
for c in pessoas:
    if c['sexo'] in 'Ff':
        mulheres.append(c["nome"])
if len(mulheres) > 0:
    print('As mulheres registradas foram : ', end = '')
    for c in mulheres:
        if mulheres.index(c) == 0:
            print(c, end='')
        elif mulheres.index(c) < len(mulheres) - 1:
            print(f', {c}', end='')
        else:
            print(f' e {c}', end='')
else:
    print('Não há mulheres registradas : ')

acimaMedia = []
for c in pessoas:
    if c['idade'] >= media:
        acimaMedia.append(c['nome'])
print('\nAs pessoas com idade acima da media foram : ', end='')
for c in acimaMedia:
    if acimaMedia.index(c) == 0:
        print(c, end='')
    elif acimaMedia.index(c) < len(acimaMedia) - 1:
        print(f', {c}', end='')
    else:
        print(f' e {c}')
