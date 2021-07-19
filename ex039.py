from datetime import date
anoh  = date.today().year
sexo  = str(input('Qual é o seu sexo? ')).strip().upper()
if sexo == 'FEMININO':
    print('Voce nao precisa se alistar :D')
elif sexo == 'MASCULINO':
    anon  = int(input('Em que ano você nasceu? '))
    idade = anoh - anon
    anoh  = date.today().year
    print(f'Você tem {idade} anos')
    if idade < 18:
        print('Não se preocupe com alistamento ainda...')
        print(f'Faltam {18 - idade} para o alistamento')
    elif idade == 18:
        print('Ano de se alistar!!!')
    elif idade > 18:
        print('Ja passou da idade necessaria!!')
        print(f'Ja se passaram {idade - 18} anos do seu alistamento')
else:
    print('Sexo invalido')
