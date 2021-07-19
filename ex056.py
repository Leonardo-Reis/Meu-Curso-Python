hmaisv = 0
contm  = 0
s = 0
for p in range(1, 5):
    print(f"{f' {p}ª Pessoa ':=^31}")
    nome  = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo  = str(input('Sexo: ')).strip().upper()
    s += idade
    if sexo == 'F' and idade < 20:
        contm += 1
    if sexo == 'M' and hmaisv == 0:
        nomev = nome
        hmaisv = idade
    elif sexo == 'M' and idade > hmaisv:
        nomev = nome
        hmaisv = idade
print(f'O homem mais velho é o {nomev.capitalize()} com {hmaisv} anos.')
print(f'{contm} mulheres mais novas que 20 anos.')
print(f'A media das idades é {s/4} anos.')
