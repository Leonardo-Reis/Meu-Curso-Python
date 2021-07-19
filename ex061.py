a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print(f'{a} -> ', end='')
    a = a + r
    c  += 1
print('FIM')