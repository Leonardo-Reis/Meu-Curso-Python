from datetime import date
anoh = date.today().year
maio = 0
meno = 0
for c in range(1, 8):
    anon = int(input('Digite o ano de nascimento: '))
    idad = anoh - anon
    if idad >= 18:
        maio += 1
    elif idad < 18:
        meno += 1
print(f'{maio} são maiores de idade.')
print(f'{meno} são menores de idade.')
