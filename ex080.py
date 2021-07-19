lista = []
for c in range(0, 5):
    n = int(input('Digite um numero para adicionar a lista: '))
    if c == 0:
        lista.append(n)
        print('Numero adicionado a lista')
    if c > 0 and n > lista[-1]:
        lista.append(n)
        print('Numero adicionado ao final da lista')
    elif c > 0 and n < lista[0]:
        lista.insert(0, n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos] and c != 0:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lsita')
                break
            pos += 1
print(lista)