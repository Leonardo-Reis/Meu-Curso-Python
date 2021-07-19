valor = int(input('Digite o valor a ser sacado: '))
n1 = n5 = n10 = n20 = n50 = 0
n50 = valor//50
valor2 = valor - n50*50
print(f'{n50} notas de R$50.')
n20 = valor2//20
valor3 = valor2 - n20*20
print(f'{n20} notas de R$20')
n10 = valor3//10
valor4 = valor3 - n10*10
print(f'{n10} notas de  R$10')
n5 = valor4//5
valor5 = valor4 - n5*5
print(f'{n5} notas de R$5')
n1 = valor4 - 5
print(f'{n1} notas de R$1')