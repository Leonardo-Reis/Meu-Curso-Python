from datetime import date
ano   = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('Nadador mirim')
elif 9 < idade <= 14:
    print('Nadador infantil')
elif 14 < idade <= 19:
    print('Nadador junior')
elif 19 < idade <= 25:
    print('Nadador Senior')
elif idade > 25:
    print('Nadador Master')
