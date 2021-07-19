s = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while s != 'M' and s != 'F':
    s = str(input('Sexo invalido. Digite novamente: ')).upper().strip()[0]
print(f'Seu sexo é {s}')
