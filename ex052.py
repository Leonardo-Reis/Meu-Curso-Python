n = int(input('Digite um numero: '))
cont = 0
for c in (2, n):
    if n % c == 0 and n != c:
        cont = cont + 1
if cont == 0:
    print('Numero primo')
elif cont != 0:
    print('Numero não é primo')
