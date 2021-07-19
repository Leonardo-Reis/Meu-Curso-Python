tupla = (int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: '))
)
print(tupla)
print(f'O 9 aparece {tupla.count(9)} vez.')
if 3 in tupla:
    print(f'O 3 esta na posição {tupla.index(3) + 1}.')
print('Os numeros pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')