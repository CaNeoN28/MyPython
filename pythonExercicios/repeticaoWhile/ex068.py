from random import randint

cont = 0
msg = 'Você perdeu!'
while True:
    opc = ''
    comp = randint(1, 10)
    player = int(input('Digite um número : '))
    while True:
        opc = input('Par ou Ímpar ?[P/I]: ')
        if opc in 'PpIi':
            break
        print('Opção inválida! Digite novamente')
    print(20 * '-=')
    res = (comp+ player) % 2
    if res == 0 and opc in 'Pp' or res == 1 and opc in 'Ii':
        msg = 'Você ganhou! Jogue de novo\n'
        cont += 1
    else:
        msg = 'Você perdeu!'
        break
    print(msg, 20 * '=-')
print(f'{msg}Seu número de vitórias é de : {cont}\n{20 * "=-"}')
