alunos = list()
count = 1
while True:
    aluno = list()
    aluno.append(input(f'Informe o nome do {count}° aluno : '))
    aluno.append(float(input(f'Informe a 1ª nota desse aluno : ')))
    aluno.append(float(input(f'Informe a 2ª nota desse aluno : ')))
    alunos.append(aluno[:])
    aluno.clear()

    opc = ''
    while True:
        opc = input('Deseja continuar? [S/N] ')[0]
        if opc in 'SsnN':
            break
        print('Opção Inválida!')
    if opc in 'Nn':
        break
    print('Então vamos continuar!')
    count += 1

media = list()
print(f'{"N°":<5}{"Nome do aluno":<20}{"Nota":>5}')
for c in alunos:
    nome = c[0]
    media.append((c[1] + c[2])/2)
    n = alunos.index(c)
    print(f'{n:<5}{nome:<20}{media[n]:>5.1f}')

while True:
    opc = int(input('Informe o número de um aluno para ver suas notas [999 para parar] : '))
    if opc == 999:
        break
    elif opc >= len(alunos):
        print('Aluno Indisponível! Tente novamente')
    else:
        print(f'Notas do aluno(a) {alunos[opc][0]}\n'
              f'Nota 1 : {alunos[opc][1]}\n'
              f'Nota 2 : {alunos[opc][2]}\n'
              f'Média  : {media[opc]}')
