def arquivoexiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'w')
        a.close()
    except:
        print('Falha ao criar um arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerarquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>5} anos')
        a.close()


def cadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('Erro ao abrir arquivo')
    else:
        try:
            a.writelines(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados.')
        else:
            print('Cadastro realizado com sucesso.')
            a.close()