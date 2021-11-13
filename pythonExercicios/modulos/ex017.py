import math

cao = float(input('Informe o comprimento do cateto oposto do triângulo : '))
caa = float(input('Informe o comprimento do cateto adjascente do triângulo : '))
hip = math.hypot(cao, caa)

print('O comprimento da hipotenusa é de {}'.format(hip))