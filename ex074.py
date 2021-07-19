from random import randint
tupla = ((randint(0, 10)), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(sorted(tupla))
print(f'O maior valor foi {max(tupla)} e o menor foi {min(tupla)}')