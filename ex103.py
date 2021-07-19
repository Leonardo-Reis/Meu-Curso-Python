def histjog(nome, gols='0'):
    if nome == '':
        nome = 'NÃO INFORMADO'
    if type(gols) != int:
        gols = '0'
    return f'O jogador {nome} fez {gols} gols.'


name = str(input('Nome do jogador: ')).strip().capitalize()
goals = str(input('Numero de gols: ')).strip()
print(histjog(name, goals))