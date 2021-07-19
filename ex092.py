from time import localtime
trabalhador = dict()
trabalhador['nome'] = str(input('Digite o nome: ')).strip().capitalize()
trabalhador['idade'] = localtime()[0] - int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho (0 caso não tenha) '))
if trabalhador['ctps'] == 0:
    print('=-'*30)
    for k, v in trabalhador.items():
        print(f'- {k} tem valor {v}')
else:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario: '))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35 - localtime()[0] + trabalhador['idade']
    print('=-'*30)
    for k, v in trabalhador.items():
        print(f'- {k} tem valor {v}')
