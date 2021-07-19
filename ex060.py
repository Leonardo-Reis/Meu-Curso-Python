n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = n
print(f'{n}!=', end='')
while c != 1:
    if c > 1:
        print(f'{c}x', end='')
    if c == 2:
        print(f'1', end='')
    if c > 0:
        n = n*(c - 1)
        c = c-1
print(f'={n}')