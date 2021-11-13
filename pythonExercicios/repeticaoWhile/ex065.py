cond = True
soma = maior = menor = count = num = 0
while cond:
    opc = input('Digite "s" se você deseja informar um número ou "n" se não : ').strip().lower()
    if opc == 's':
        num = float(input('Informe o {}° número : '.format(count+1)))
        soma += num
        count += 1
    elif opc == 'n':
        cond = False
    else:
        print('Opção inválida! Digite novamente!')

    if count == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num

media = soma/count
print('O maior e o menor dos {} valores são, respectivamente, {} e {}'
      '\nA média dos valores é {:.2f}'.format(count, maior, menor, media))
