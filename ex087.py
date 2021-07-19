matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o numero ({l},{c}): '))
print('=-'*30)
for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end='')
    print()
print('=-'*30)
for l in matriz:
    for c in l:
        if c % 2 == 0:
            pares.append(c)
cont = 0
for n in matriz[1]:
    if cont == 0:
        maior = n
    if cont >= 1:
        if n > maior:
            maior = n
    cont += 1
s = 0
for l in matriz:
    s += l[2]
print(f'pares: {pares}')
print(f'Maior valor da linha 2: {maior}')
print(f'Soma dos valores da coluna 3: {s}')


