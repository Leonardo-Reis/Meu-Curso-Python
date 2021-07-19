def fatorial(num, show=False):
    """
    -> Calcula o referencial
    :param num: Numero que você quer achar o fatorial.
    :param show: Se quer mostrar as contas ou não.
    :return: Fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f"{c}x", end='')
            else:
                print(f"{c}=", end='')
        f *= c
    return f


print(fatorial(8))
help(fatorial)