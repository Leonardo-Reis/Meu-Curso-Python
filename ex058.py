from random import randint
cont = 1
bot = randint(0, 10)
num = int(input('Tente adivinhar o numero entre 0 e 10: '))
while num != bot:
    if num > bot:
        num = int(input('Menos... Tente novamente: '))
    if num < bot:
        num = int(input('Mais... Tente novamente: '))
    cont += 1
print(f'Acertou! Você tentou {cont} vezes')