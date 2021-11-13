while True:
    num = int(input('Digite um número para ver a tabuada : '))
    print(20 * '=')
    cont = 1

    if num < 0:
        break
    while True:
        print(f'{num} x {cont:>2} = {num * cont}')
        cont += 1
        if cont > 10:
            break
    print(20 * '=')
print('Tenha um bom dia!')
