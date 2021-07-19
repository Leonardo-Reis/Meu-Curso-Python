s = contmil = maiorp = 0
nomec = ''
while True:
    op = ''
    print('='*30)
    nome = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('preço do produto: R$'))
    s += preco
    if preco >= 1000:
        contmil += 1
    if maiorp == 0:
        maiorp = preco
        nomec = nome
    if preco > maiorp:
        maiorp = preco
        nomec = nome
    while op != 'N' and op != 'S':
        op = str(input('Deseja adicionar mais um produto? [S/N] ')).upper().strip()
    if op == 'N':
        break
print(f'O valor total foi de R${s}.')
print(f'Você escolheu {contmil} valores acima de R$1000.')
print(f'O produto mais caro foi {nomec.capitalize()} custando R${maiorp}')