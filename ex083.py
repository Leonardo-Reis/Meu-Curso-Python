lista = []
exp = str(input('Digite uma expressão: '))
cont1 = cont2 = 0
for char in exp:
    if char == '(':
        cont1 += 1
    if char == ')':
        cont2 += 1
if cont1 == cont2:
    print('Expressão valida')
else:
    print('Expressão invalida')