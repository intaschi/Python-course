import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] +35) - datetime.date.today().year
print('=-' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')