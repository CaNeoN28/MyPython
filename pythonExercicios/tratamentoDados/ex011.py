alt = float(input('Informe a altura da parede : '))
lar = float(input('Informe a largura da parede : '))

area = alt*lar
tint = area/2

print('Para pintar essa parede com {}m² são necessários {:.2f}L de tinta'.format(area, tint))
