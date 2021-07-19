from random import randint
from time import sleep
listao = []
listinha = []
cont = 0
num_palp = int(input('Quantos palpites você quer? '))
while cont != num_palp:
    while True:
        n = randint(1, 60)
        if n not in listinha:
            listinha.append(n)
        if len(listinha) == 6:
            listinha.sort()
            listao.append(listinha)
            listinha = []
            break
    cont += 1
for palp in listao:
    print(palp)
    sleep(1)
print("=-"*15)
print(f'{"Boa Sorte":^30}')
print('=-'*15)