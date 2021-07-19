lista = []
maior = menor = 0
posm = posM = 0
for n in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
for c, v in enumerate(lista):
    if c == 0:
        maior = v
        menor = v
        posM = c
        posm = c
    if c > 0 and v > maior:
        maior = v
        posM = c
    if c > 0 and v < menor:
        menor = v
        posm = c
print(f'O maior numero foi o {maior} na posição {posM + 1}\nO menor numero foi o {menor} na posição {posm + 1}')