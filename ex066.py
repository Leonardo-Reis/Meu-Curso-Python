cont = s = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} numero e a sua soma é {s}')