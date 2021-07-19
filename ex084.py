pessoa = list()
grupo = list()
s = 0
maiorp = list()
menorp = list()

while True:
    nome = str(input('Digite o nome: ')).capitalize()
    peso = float(input('Digite seu peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    if s == 0:
        maiorp = menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
    s += 1
    grupo.append(pessoa[:])
    pessoa = []
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while op not in 'SN':
        op = str(input('Opção invalida. Tente novamente: ')).strip().upper()
    if op == 'N':
        break
print(grupo)
print(f'{s} pessoas foram cadastradas.')
print(f'O maior peso foi {maiorp}Kg', end=' ')
for p in grupo:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print(f'O menor peso foi {menorp}Kg', end=' ')
for p in grupo:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')
