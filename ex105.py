def notas(*nots, sit=False):
    """
    -> Função para analisar notas de varios alunos
    :param nots: notas dos alunos
    :param sit: Sittuação do aluno (Reprovado/Aprovado)
    :return: Dicionario com as informações do aluno
    """
    aluno = dict()
    maior = menor = nots[0]
    soma = 0
    for c in nots:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        soma += c
    aluno['Maior'] = maior
    aluno['Menor'] = menor
    aluno['Media'] = soma/len(nots)
    if sit:
        if aluno['Media'] >= 7:
            aluno['Situação'] = 'Aprovado'
        elif aluno['Media'] <= 7:
            aluno['Situação'] = 'Reprovado'
    return aluno


print(notas(5, 7, 8, sit=True))
help(notas)
