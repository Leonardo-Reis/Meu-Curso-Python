jogador = dict()
lista_gols = list()
lista_jogadores = list()
s = 0
while True:
    jogador.clear()
    lista_gols.clear()
    s = 0
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    for c in range(1, jogos + 1):
        gol = int(input(f' - Quantos gols {jogador["nome"]} fez no jogo {c}? '))
        lista_gols.append(gol)
        s += gol
    jogador['gols'] = lista_gols[:]
    jogador['total'] = s
    lista_jogadores.append(jogador.copy())
    print("-="*30)
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while op not in 'SN':
        op = str(input('Opção errada. Digite S ou N: ')).strip().upper()
        if op in 'SN':
            break
    if op == 'N':
        break
print("-="*30)
print(lista_jogadores)
print("-="*30)
print(f'{"id":<5}{"nome":<10}{"gols":<10}{"total":>10}')
print('='*40)
for c, p in enumerate(lista_jogadores):
    print(f'{c:<5}{p["nome"]:<10}{str(p["gols"]):<10}{p["total"]:>10}')
print('='*40)
while True:
    jog = int(input('Deseja ver os gols de quais jogaodor? (999 para) '))
    while jog not in range(0, len(lista_jogadores)) and jog != 999:
        jog = int(input('ERRO! Digite um id de jogador valido: '))
    if jog == 999:
        break
    for c in range(0, len(lista_jogadores[jog]["gols"])):
        print(f'No jogo {c + 1}, {lista_jogadores[jog]["nome"]} fez {lista_jogadores[jog]["gols"][c]}')
    print('-='*30)
