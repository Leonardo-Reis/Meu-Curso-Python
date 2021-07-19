from time import sleep


def contador(a0, an, r):
    if r == 0:
        r = 1
    if an < a0 and r > 0:
        r = r*-1
    if an < a0:
        an = an - 2
    for c in range(a0, an + 1, r):
        print(c, end=' ')
        sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 1, 1)
primeiro = int(input('Primeiro termo: '))
ultimo = int(input('Ultimo termo: '))
razao = int(input('Razão: '))
contador(primeiro, ultimo, razao)
