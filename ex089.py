aluno = []
notas = []
alunos = []
op = ''
while True:
    nome = str(input('Nome do aluno: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    aluno.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(notas)
    aluno.append(media)
    alunos.append(aluno)
    aluno = []
    notas = []
    op = str(input('Deseja continuar: [S/N] ')).strip().upper()
    while op not in 'SN':
        op = str(input('Opção invalida. Digite novamente: ')).strip().upper()
    if op == 'N':
        break
print(alunos)
print()
print(f'{"id":<5}{"Nome":<10}{"Media":>10}')
print('='*30)
for c in range(0, len(alunos)):
    print(f'{c:<5}{alunos[c][0]:<10}{alunos[c][2]:>10.1f}')
print('='*30)
while True:
    opn = str(input('Mostrar notas de qual aluno? (999 para parar) ')).strip().capitalize()
    for aluno in alunos:
        if aluno[0] == opn:
            print(f'As notas de {aluno[0]} foram {aluno[1]}')
    print("-" * 40)
    if opn == '999':
        break
