from time   import sleep
from random import randint
print(f"{' JOKENPO BRABO ':=^40}")
print('''Suas opções:
[ 1 ] Pedra 
[ 2 ] Papel
[ 3 ] Tesoura''')
mao = int(input('Digite sua opção: '))
bot = randint(1, 3)
if bot == 1:
    bot = 'pedra'
elif bot == 2:
    bot = 'papel'
elif bot == 3:
    bot = 'tesoura'
if mao == 1:
    mao = 'pedra'
elif mao == 2:
    mao = 'papel'
elif mao == 3:
    mao = 'tesoura'
if mao == 'pedra' or mao == 'papel' or mao == 'tesoura':
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    print(f"{'='*23}")
    print(f'''Você usou {mao}
Computador usou {bot}''')
    print(f"{'='*23}")
    if mao == bot:
        print('EMPATE!')
    elif (mao == 'pedra' and bot == 'tesoura') or (mao == 'papel' and bot == 'pedra') or (mao == 'tesoura' and bot == 'papel'):
        print('Você ganhou!! :D')
    else:
        print('Você perdeu :/')
else:
    print('Opção invalida. Tente novamente.')
    