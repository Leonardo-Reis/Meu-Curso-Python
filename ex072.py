numeroex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quineze',)
while True:
    n = int(input('Digite um numero de 0 a 20: '))
    if 0 <= n <= 15:
        break
print(f'Você digitou o numero {numeroex[n]}')