aluno = {}
aluno['nome'] = input('Informe o nome de um aluno : ')
aluno['média'] = float(input('Informe sua média : '))
aluno['situação'] = ''

if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print(f'O nome do aluno é {aluno["nome"]}\n'
      f'Sua média é {aluno["média"]}\n'
      f'E sua situação é {aluno["situação"]}!')