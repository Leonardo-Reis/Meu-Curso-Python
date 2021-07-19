def voto(ano):
    from time import localtime
    idade = localtime()[0] - ano
    if idade < 16:
        return f'{idade} anos. Votação negada.'
    elif 18 > idade >= 16:
        return f'{idade} anos. Votação opcional.'
    elif idade >= 18:
        return f'{idade} anos. Voto obrigatorio '


nasc = int(input('Seu ano de nascimento: '))
print(voto(nasc))
