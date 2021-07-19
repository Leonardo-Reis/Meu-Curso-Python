import moeda

p = float(input('Digite o preço: '))
print(f'O dobro do preço é {moeda.dobro(p, format=True)}')
print(f'O triplo do preço é {moeda.triplo(p, format=True)}')
print(f'Aumentando 10% temos {(moeda.aumentar(p, 10, format=True))}')
print(f'Diminuindo 30% temos {moeda.diminuir(p, 30, format=True)}')