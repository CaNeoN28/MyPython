sum = 0
count = 0
nomeV = ''
idadeV = 0
mVinte = 0

for c in range(1, 5):

    cond = True

    while True:
        nome = input('Informe o nome da {}° pessoa : '.format(c)).strip()
        idade = int(input('Informe a idade dessa pessoa : '))
        sexo = input('Informe o sexo dessa pessoa (digite m para masculino e f para feminino) : ').lower()
        if (sexo != 'f' and sexo != 'm'):
            print('Sexo inválido!')
        else:
            cond = False
    sum += idade
    count += 1
    if(sexo == 'm'):
        if(nomeV == ''):
            nomeV = nome
            idadeV = idade
        elif(idade > idadeV):
            nomeV = nome
            idadeV = idade
    elif(idade <= 20):
        mVinte += 1

if(nomeV != ''):
    print('O nome do homem mais velho é {} com {} anos de idade'.format(nomeV, idadeV))
else:
    print('Não há homens no grupo')
if(mVinte != 0):
    print('O número de mulheres de até 20 anos é de : {}'.format(mVinte))
else:
    print('Não há mulheres com até 20 anos no grupo')
print('A média das idades dos membros do grupo é de : {}'.format(sum/count))