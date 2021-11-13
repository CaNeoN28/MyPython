def leiaDinheiro(msg):
    while True:
        valor = str(input(msg))
        aux = valor
        if ',' in valor:
           aux = aux.replace(',', '.')
        if aux.isnumeric() or '.' in aux:
           break
        print(f'\"{valor}\" é um valor inválido!')
    return valor
