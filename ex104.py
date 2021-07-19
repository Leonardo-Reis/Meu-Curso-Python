def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print('Digite um numero inteiro valido.')
    return num


n = leiaInt('Digite um numero inteiro: ')
print(f'Você digitou {n}')