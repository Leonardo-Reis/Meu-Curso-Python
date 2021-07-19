from pack115.interface import titulo, opcoes, leiaint
from pack115.arquivos import arquivoexiste, criararquivo, lerarquivo, cadastro
from time import sleep

arquivo = 'cadastro115.txt'

if arquivoexiste(arquivo):
    print('Arquivo existe.')
else:
    print(f'Arquivo {arquivo} não existe.')
    criararquivo(arquivo)

while True:
    titulo('MENU PRINCIPAL')
    op = opcoes()
    if op == 3:
        break
    elif op == 2:
        titulo('Novo Cadastro')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaint('Idade: ')
        cadastro(arquivo, nome, idade)
    elif op == 1:
        titulo('Pessoas Cadastradas')
        lerarquivo(arquivo)
    sleep(2)