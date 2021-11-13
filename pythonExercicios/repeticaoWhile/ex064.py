sum = num = count = 0

while num != 999:
    num = int(input('Informe um número (insira 999 para sair): '))
    if num != 999:
        count += 1
        sum += num

print('Você digitou {} números e a soma deles é {}!\nTenha um bom dia!'.format(count, sum))