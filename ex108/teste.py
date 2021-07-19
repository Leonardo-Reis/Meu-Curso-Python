import moeda

p = float(input('Digite o preço: '))
print(f'O dobro do preço é {moeda.moeda(moeda.dobro(p))}')
print(f'O triplo do preço é {moeda.moeda(moeda.triplo(p))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 30% temos {moeda.moeda(moeda.diminuir(p, 30))}')