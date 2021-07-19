from random import randint
lista = list()
listapar = list()


def sorteia():
    cont = 0
    while True:
        lista.append(randint(0, 11))
        cont += 1
        if cont == 5:
            break
    print(lista)


def somapar():
    cont = s = 0
    for n in lista:
        if n % 2 == 0:
            listapar.append(n)
    for n in listapar:
        s += n
    print(f'A soma dos valores pares da lista são: {s}')


sorteia()
somapar()
