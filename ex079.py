op = ''
lista = []
while True:
    n = int(input('Digite um numero para adicionar a lista: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Numero não adicionado, ja esta na lista...')
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if op == 'N':
        break
print(sorted(lista))