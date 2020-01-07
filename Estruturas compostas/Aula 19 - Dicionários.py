dados = {}
dados = dict()
dados = {'nome':'Carol', 'idade':23}
print(f'A {dados["nome"]} tem {dados["idade"]} anos')
dados['sexo'] = 'f'
print(dados.values())
del dados['sexo']
dados['nome'] = 'Caroline'
print(dados.keys())
print(dados.items())
for c in dados.values():
    print(c)
for c in dados.keys():
    print(c)
for k, v in dados.items():
    print(k)
    print(v)

Brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'Sigla':'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil[0]['uf'])

pais = list()
estado = dict()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    pais.append(estado.copy())
for e in pais:
    for k, v in e.items:
        print(f'O campo {k} tem valor {v}')


