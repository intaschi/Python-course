dados = {}
lista = []
while True:
    dados['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    if sexo not in 'FM':
        print('INVÁLIDO. Responda apenas F ou M.')
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
    else:
        dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    dados.clear()
    resp = str(input('QUER CONTINUAR [S/N]? ')).strip().upper()
    if resp not in 'SN':
        print('INVÁLIDO. Responda apenas S ou N.')
        resp = str(input('QUER CONTINUAR [S/N]? ')).strip().upper()
    elif resp == 'N':
        break
print('=-' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média das idades é igual a ', end='')
soma = 0
for c in range(0, len(lista)):
    soma += lista[c]['idade']
print(f'{soma/len(lista):.2f}')
print(f'C) As mulheres cadastradas foram: ')
for c in lista:
    if c['sexo'] in 'F':
        print(f'{c["nome"]} ', end='')
print('\nD) Lista das pessoas que estão acima da média: ')
for c in range(0, len(lista)):
    if lista[c]['idade'] > soma/len(lista):
        for k, v in lista[c].items():
            print(f'    {k} = {v} ', end='')
        print()
print('>>> ENCERRADO <<<')