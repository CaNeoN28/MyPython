def nota(*lst, sit = False):
    '''
    Retorna valores relacionados às notas de vários alunos de uma turma
    :param lst: Notas de um ou vários alunos
    :param sit: Se verdadeiro, retorna também a situação geral da turma (Padrão = False)
    :return: Dicionário com as diversas informações da turma
    '''

    dic = {}
    dic['Total'] = len(lst)
    dic['Maior'] = max(lst)
    dic['Menor'] = min(lst)
    dic['Média'] = f'{(sum(lst) / len(lst)):.2f}'
    if sit:
        media = float(dic['Média'])
        if media >= 7:
            dic['Situação'] = 'BOA'
        elif media >= 6:
            dic['Situação'] = 'RAZOÁVEL'
        else:
            dic['Situação'] = 'RUIM'
    return(dic)


nota = nota(8.8, 7.9, sit=True)
print(nota)