a1 = int(input('Digite o primeiro termo: '))
r  = int(input('Digite a razão: '))
print(f'{a1} ->', end=' ')
for c in range(1, 11):
    a1 += r
    print(f'{a1} -> ', end=' ')
    if c == 10:
        print('ACABOU!!')
