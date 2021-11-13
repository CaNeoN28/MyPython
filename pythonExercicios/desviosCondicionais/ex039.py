from datetime import date

ano = int(input('Informe seu ano de nascimento: '))
id = date.today().year - ano

if(id > 18):
    print('Ja passou do tempo de se alistar!\nVocê está atrasado há {} anos'.format(ano - 18))
elif(id == 18):
    print('Está na hora de você se alistar!')
else:
    print('Você ainda vai precisar se alistar!\nFalta {} anos para você se alistar'.format(18 - ano))
