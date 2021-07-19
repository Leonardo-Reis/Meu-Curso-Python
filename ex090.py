aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).capitalize().strip()
aluno['media'] = float(input('Digite a media do aluno: '))
print(f'- Nome do aluno: {aluno["nome"]}')
print(f'- Media do aluno: {aluno["media"]}')
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'- Situação: {aluno["situacao"]}')