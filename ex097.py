def print2(msg):
    print('='*(len(msg) + 2))
    print(f' {msg}')
    print('='*(len(msg) + 2))


mensagem = str(input('Escreva a mensagem: '))
print2(mensagem)
