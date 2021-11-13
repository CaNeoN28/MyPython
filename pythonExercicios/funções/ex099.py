from time import sleep


def maior(*lst):
    print('-' * 50)
    print('Analisando valores...')
    for c in lst:
        print(c, end=' ')
        sleep(0.5)
    print(f'foram analisados, número de valores : {len(lst)}')
    sleep(1)
    maior = 0
    if len(lst) > 0:
        maior = max(lst)
    print(f'O maior valor informado foi {maior}')
    sleep(1)


maior(4, 7, 1, 3, 5)
maior(3, 5, 6, 7, 7, 2)
maior(6, 9, 1, 3)
