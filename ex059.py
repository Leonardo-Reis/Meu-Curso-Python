op = 0
while op != 5:
    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero:  '))
    print('O que deseja fazer com esses dois numeros?')
    print(f"{'':=^20}")
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Fechar programa''')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print(f'Resultado da soma: {n1 + n2}')
    if op == 2:
        print(f'Resultado da multiplicação: {n1*n2}')
    if op == 3:
        if n1 > n2:
            print('O primeiro é maior')
        elif n2 > n1:
            print('O segundo é maior')
        else:
            print('Numeros iguais')
    print(f"{'':=^20}")