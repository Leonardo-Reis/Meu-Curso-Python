num = ('Biscoito', 5.50, 'Leite', 8.0, 'Café', 6.0, 'Chocolate', 5.0)
print('='*20)
print(f'{"LOJAS BRABO":^20}')
print('='*20)
for c in range(0, len(num)):
    if c % 2 == 0:
        print(f'{num[c]:.<17}', end='')
    if c % 2 != 0:
        print(f'{num[c]}')