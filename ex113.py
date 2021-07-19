def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print('ERRO, digite um numero inteiro.')
    return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
            break
        except ValueError:
            print('ERRO, digite um numero real.')
    return num


n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real: ')
print(f'Você digitou o numeor inteiro {n1} e o numero real {n2}')
