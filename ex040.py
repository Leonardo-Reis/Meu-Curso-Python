n1  = float(input('Primeira nota: '))
n2  = float(input('Segunda nota:  '))
med = (n1 + n2)/2
print(f'Sua media final é {med:.2f}.')
if med < 5:
    print('Reprovado :/')
elif 5 <= med < 6.9:
    print('Em recuperação.')
elif med >= 7:
    print('Aprovado!!')