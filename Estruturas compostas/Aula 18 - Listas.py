teste = list()
teste.append('Carol')
teste.append(40)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Gustavo'
teste[1] = 25
galera.append(teste[:])
print(galera)

galera = [['joão', 33], ['Maria', 12], ['Joaquim', 20]]
print(galera[0][0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')

galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] > 21:
        print(f'O {p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'O {p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
