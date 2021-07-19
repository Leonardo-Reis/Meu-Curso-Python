pessoa = dict()
grupo = list()
cont = 0
soma_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: ')).strip().capitalize()
    sexo = str(input('Digite o sexo [M/F] ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Opção invalida. Digite M ou F: ')).strip().upper()
        if sexo in 'MF':
            break
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Digite a idade: '))
    cont += 1
    soma_idade += pessoa['idade']
    grupo.append(pessoa.copy())
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while op != 'S' and op != 'N':
        op = str(input('Opção invalida. Digite S ou N: ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
media = soma_idade/cont
print("-="*30)
print(grupo)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A media da idades é {media:.2f}.')
print(f'C) Mulheres cadastradas: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('Pessoas com idade acima da media:')
for p in grupo:
    if p['idade'] > media:
        print(f' - nome = {p["nome"]} | sexo = {p["sexo"]} | idade = {p["idade"]}')
