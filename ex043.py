pes = float(input('Seu peso em Kg: '))
alt = float(input('Sua altura em metros: '))
imc = pes/(alt**2)
print(f'Seu imc é {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 25 > imc >= 18.5:
    print('Peso ideal.')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 > imc >= 30:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade morbida!')