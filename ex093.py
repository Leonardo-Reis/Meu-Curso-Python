jogador = dict()
lista_gols = list()
s = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
for c in range(1, jogos + 1):
    gol = int(input(f'   Quantos gols {jogador["nome"]} fez no jogo {c}? '))
    lista_gols.append(gol)
    s += gol
jogador['gols'] = lista_gols
jogador['total'] = s
print("-="*30)
print(jogador)
print("-="*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print("-="*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for c in range(0, jogos):
    print(f'  =>Na partida {c + 1} {jogador["nome"]} fez {jogador["gols"][c]} gols')
print(f'Total de {s} gols')
