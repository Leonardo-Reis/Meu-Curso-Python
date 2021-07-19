contm = cont18 = contif = idade = 0
sexo = ''
while True:
    op = ''
    sexo = ''
    idade = 0
    print('='*30)
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()[0]
    if sexo == 'M':
        contm += 1
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        cont18 += 1
    if sexo == 'F' and idade < 20:
        contif += 1
    while op != 'S' and op != 'N':
        op = str(input('deseja continuar? [S/N] ')).upper().strip()
    if op == 'N':
        break
print(f'Foram registrados {contif} mulheres mais novas que 20 anos. ')
print(f'Foram registrados {cont18} pessoas maiores de 18 anos.')
print(f'Foram registrados {contm} Homens.')