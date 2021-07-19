def maimen(*num):
    cont = 0
    maior = menor = 0
    while True:
        if num == ():
            break
        if cont == 0:
            maior = menor = num[0]
        if num[cont] > maior:
            maior = num[cont]
        elif num[cont] < menor:
            menor = num[cont]
        cont += 1
        if cont == len(num) - 1:
            break
    print(f'Maior: {maior}\nMenor: {menor}')
    print('+-'*15)


maimen(2, 5, 7, 8)
maimen(-2, 3, 6, 12)
maimen()