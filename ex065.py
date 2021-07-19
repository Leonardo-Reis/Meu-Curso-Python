s = cont = menor = maior = 0
resp = 'S'
while resp == 'S':
    n = int(input('Digite um numero: '))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    s += n
    cont +=1
    if maior == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f'Você digitou {cont} numeros e a sua media é {s/cont}.')
print(f'O maior numero foi {maior} e o menor foi {menor}')
