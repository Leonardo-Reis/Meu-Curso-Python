l1 = int(input('Primeiro lado: '))
l2 = int(input('Segundo lado:  '))
l3 = int(input('Terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Triangulo existe.')
    if l1 == l2 == l3:
        print('Triangulo equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triangulo isosceles')
    elif l1 != l2 != l3:
        print('Triangulo escaleno')
else:
    print('Triangulo nao existe')