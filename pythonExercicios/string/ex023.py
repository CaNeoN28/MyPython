num = int(input('Inform um número entre 0 e 9999 : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
'''manipulação de string é meu ovo'''

print('Unidade : {}'.format(u))
print('Dezena : {}'.format(d))
print('Centena : {}'.format(c))
print('Milhar : {}'.format(m))