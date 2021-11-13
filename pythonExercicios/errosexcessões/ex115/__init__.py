def Titulo(msg):
    print('~~' * 30)
    print(f'{msg:^60}')
    print('~~' * 30)


arquivo = 'pessoas.txt'


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'r')
        a.close()
    except FileNotFoundError:
        a = open(arquivo, 'w')
        a.close()


def Cadastrar():
    while True:
        Titulo('CADASTRO')
        try:
            nome = str(input('Digite o nome da pessoa a ser cadastrada : '))
            idade = int(input('Informe a idade dessa pessoa : '))

            arquivoExiste(arquivo)

            ref_arquivo = open('pessoas.txt', 'at')
            ref_arquivo.write(f'{nome};{idade};\n')
            ref_arquivo.close()
            break
        except ValueError:
            print('\033[031mERRO : O valor informado não é válido!\033[m')


def Listar():
    Titulo('LISTAGEM')

    ref_arquivo = open('pessoas.txt', 'r')
    for c in ref_arquivo:
        valor = c.split(';')
        valor[1] += ' anos'
        print(f'{valor[0]:<40}{valor[1]:>20}')
    ref_arquivo.close()
