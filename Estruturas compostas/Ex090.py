dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] < 5:
    dados['situação'] = 'REPROVADA'
else:
    dados['situação'] = 'APROVADA'
for k, v in dados.items():
    print(f'{k} é igual a {v}')

