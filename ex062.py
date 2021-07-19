a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print(f'{a} -> ', end='')
    a = a + r
    c  += 1
cont = c
print('PAUSA')
c = 1
op = int(input('Mais quantos termos você deseja ver? '))
while op != 0:
    while c <= op:
        print(f'{a} -> ', end='')
        a += r
        c += 1
        cont += 1
        if c == op + 1:
            print('PAUSA')
    op = int(input('Mais quantos termos você deseja ver? '))
    c = 1
print('FIM')
print(f'{cont - 1} numeros foram mostrados')