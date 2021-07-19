def titulo(msg):
    print('-'*30)
    print(msg.center(30))
    print('-'*30)


def opcoes():
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema''')
    print('-'*30)
    while True:
        try:
            while True:
                op = int(input('Sua opção: '))
                if op in range(1, 4):
                    break
                else:
                    print('ERRO! Digite uma opção existente.')
            break
        except ValueError:
            print('ERRO! Digite um numero inteiro valido.')
    return op


def cadastro():
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print('ERRO, digite um numero inteiro.')
    return num