nota1 = float(input('Informe sua primeira nota : '))
nota2 = float(input('Informe sua segunda nota : '))
media = (nota1 + nota2)/2

print('Com média {:.1f} sua situação é : '.format(media))
if 7 > media >= 5:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')