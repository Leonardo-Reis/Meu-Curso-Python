c = 0
cont = 0
s = 0
while c != 999:
    c = int(input('Digite um numero (999 para parar): '))
    if c != 999:
        cont += 1
        s += c
print(f'Voce digitou {cont} numeros que somados da {s}')
