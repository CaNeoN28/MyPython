def voto(ano = 0):
    from datetime import datetime
    idade = datetime.now().year - ano
    msg = f'Com a idade de {idade} anos, o voto é '
    if 18 <= idade < 60:
        msg += 'OBRIGATÓRIO'
    elif idade >= 16:
        msg += 'OPCIONAL'
    else:
        msg += 'NEGADO'
    return msg


ano = int(input('Informe seu ano de nascimento : '))
print(voto(ano))
