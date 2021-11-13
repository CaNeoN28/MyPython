from datetime import date

id = date.today().year - int(input('Informe o ano de nascimento de um atleta: '))
msg = ''

if(id <= 9):
    msg = 'MIRIM'
elif(id <= 14):
    msg = 'INFANTIL'
elif(id <= 19):
    msg = 'JUNIOR'
elif(id == 20):
    msg = 'SÊNIOR'
else:
    msg = 'MASTER'

print('Com idade igual à {} esse atleta é : {}'.format(id,msg))
