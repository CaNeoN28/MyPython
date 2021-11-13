from datetime import datetime

pessoa = {}
pessoa['nome'] = input('Informe o nome de uma pessoa : ')
pessoa['idade'] = datetime.today().year - int(input('Informe o ano de nascimento dessa pessoa : '))
pessoa['ctps'] = int(input('Informe o número de sua carteira de trabalho (0 se não tiver): '))

if pessoa['ctps'] != 0:
    min = 60
    pessoa['contratação'] = int(input('Informe o ano de contratação : '))
    cont = 15 - (datetime.today().year - pessoa['contratação']) + pessoa['idade']
    pessoa['salario'] = 'R$' + str(float(input('Informe o salário da pessoa : R$')))

    if cont > 60:
        pessoa['aposentadoria'] = cont
    else:
        pessoa['aposentadoria'] = min

for k, c in pessoa.items():
    print(f'{k} tem valor {c}')

