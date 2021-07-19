def aumentar(num=0, taxa=0, format=False):
    result: float = num + (taxa / 100) * num
    if format:
        return moeda(result)
    else:
        return result


def diminuir(num=0, taxa=0, format=False):
    result = num - (taxa/100)*num
    if format:
        return moeda(result)
    else:
        return result


def dobro(num=0, format=False):
    result = num*2
    if format:
        return moeda(result)
    else:
        return result


def triplo(num=0, format=False):
    result = num*3
    if format:
        return moeda(result)
    else:
        return result


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
