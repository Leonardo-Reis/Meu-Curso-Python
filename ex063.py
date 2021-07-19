n = int(input('Quantos termos da sequencia de fibonacci você deseja ver? '))
c = 3
a1 = 0
a2 = 1
print(f'{a1} -> {a2} -> ', end='')
an = 0
while c <= n:
    an = a1 + a2
    print(f'{an} -> ', end='')
    c += 1
    a1 = a2
    a2 = an
print('fim')
