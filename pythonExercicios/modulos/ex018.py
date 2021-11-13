from math import tan, cos, sin, radians

ang = int(input('Informe a medida de um ângulo : '))
rad = radians(ang)
a = tan(rad)
b = cos(rad)
c = sin(rad)

print('O seno do ângulo {}° é de {}'.format(ang, c))
print('O cosseno do ângulo {}° é de {}'.format(ang, b))
print('A tangente do ângulo {}° é de {}'.format(ang, a))