from datetime import date

mai = 0
men = 0
for c in range(0, 7):
    ano = int(input('Informe o ano de nascimento de uma pessoa : '))
    idade = date.today().year - ano

    if(idade >= 18):
        mai += 1
    else:
        men += 1

print('O número de pessoas em maioridade é de : {}'.format(mai))
print('O número de pessoas em menoridade é de : {}'.format(men))
