print(30 * '=')
print(f'{"Banco da esquina":^30}')
print(30 * '=')

céd = [1, 10, 20, 50]
valor = int(input('Informe um valor para saque : '))
msg = ''
aux = len(céd) - 1

while True:
    num = 0
    while valor >= céd[aux]:
        num += 1
        valor -= céd[aux]
    if num > 0:
        msg += f'O número de cédulas de R${céd[aux]} foi de : {num}\n'
    aux -= 1
    if valor == 0:
        break
print(msg)
