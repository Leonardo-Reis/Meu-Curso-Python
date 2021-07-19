def aumentar(num=0, taxa=0):
    return num + (taxa/100)*num


def diminuir(num=0, taxa=0):
    return num - (taxa/100)*num


def dobro(num=0):
    return num*2


def triplo(num=0):
    return num*3


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
