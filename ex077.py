palavras = ('Amanha', 'Pneu', 'Dia', 'Trabalho', 'Leonardo')
for c in palavras:
    print(f'\nNa palavra {c} temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')