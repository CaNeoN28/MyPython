cond = True
while cond:
    sexo = input('Digite F para feminino'
                 '\nDigite M para masculino'
                 '\nInforme o sexo de uma pessoa : ').strip()
    if sexo not in 'MmFf':
        cond = False
    else:
        print('Sexo inválido !'
              '\nDigite novamente')