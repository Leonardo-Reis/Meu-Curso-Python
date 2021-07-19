lista = []
cont  = 0
op = ''
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while op not in 'SN':
        op = str(input('Opção invalida. Deseja continuar? [S/N] ')).strip().upper()
    if op == 'N':
        break
print(f"Voce digitou {len(lista)} numeros")
print(f"Voce digitou os numeros: {lista}")
if 5 in lista:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')
lista.sort()
print(lista)