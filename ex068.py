from random import randint
contv = 0
print('='*30)
print(f"{'JOGO PAR OU IMPAR':^30}")
print('='*30)
while True:
    bot = randint(1, 10)
    mao = int(input('Digite seu numero: '))
    poi = str(input('Par ou Impar: ')).strip().upper()
    if ((bot + mao) % 2 == 0 and poi == 'P') or ((bot + mao) % 2 != 0 and poi == 'I'):
        print(f'O computador escolheu {bot} e você {mao}, você ganhou!! :D')
        contv += 1
    else:
        print(f'O computador escolheu {bot} e você {mao}, você perdeu. :/')
        break
print(f'Você ganhou {contv} vezes.')
