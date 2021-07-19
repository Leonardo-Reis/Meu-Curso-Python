from random   import randint
from time     import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} sorteou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i + 1}º {v[0]} tirou {v[1]}')
    sleep(1)
