def notas(*n, sit=False):
    """
    Função para analisar notas e situação de um aluni.
    n = uma ou mais notas de um aluno (aceita várias)
    sit = mostra a situação do aluno (opicional)
    """
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n)/len(n)
    if sit:
        if sum(n)/len(n) < 5:
            dic['Situação'] = 'REPROVADO'
        else:
            dic['Situação'] = 'APROVADO'
    return dic


#programa principal
resp = notas(3, 4, 6, 8, sit=True)
print(resp)
