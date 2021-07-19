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


def resumo(num=0, taxaa=10, taxar=10, format=False):
    print('-'*30)
    print('RESUMO'.center(30))
    print('-'*30)
    print(f'Valor: \t\t\t\t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, format=format)}')
    print(f'Triplo do valor: \t{triplo(num, format=format)}')
    print(f'Aumento de {taxaa}%: \t{aumentar(num, taxaa, format=format)}')
    print(f'Redução de {taxar}%: \t{diminuir(num, taxar, format=format)}')
    print('-'*30)