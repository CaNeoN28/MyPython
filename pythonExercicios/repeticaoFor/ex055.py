mai = 0
men = 0

for c in range(1, 6):
    peso = float(input('Informe o peso da {}° pessoa : '.format(c)))
    if c == 1:
        mai = peso
        men = peso
    else:
        if peso >= mai:
            mai = peso
        elif peso <= men:
            men = peso

print('O maior e o menor peso são {:.2f}kg e {:.2f}kg, respectivamente'.format(mai, men))
