lista  = []
listap = []
listai = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    if n % 2 != 0:
        listai.append(n)
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while op not in 'SN':
        op = str(input('Opção invalida. Deseja continuar? ')).upper().strip()
    if op == 'N':
        break
lista.sort()
listai.sort()
listap.sort()
print(f'Voce digitou os numeros {lista}')
print(f'{listap} sao pares')
print(f'{listai} sao impares')
