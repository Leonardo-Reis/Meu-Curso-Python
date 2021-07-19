import moeda

p = float(input('Digite o preço: '))
print(f'O dobro do preço é R${moeda.dobro(p)}')
print(f'O triplo do preço é R${moeda.triplo(p)}')
print(f'Aumentando 10% temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 30% temos R${moeda.diminuir(p, 30)}')