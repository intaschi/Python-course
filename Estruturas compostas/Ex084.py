pessoa = list()
auxilio = list()
pesada = leve = 0
pp = list()
pl = list()
while True:
    auxilio.append(input('Nome: '))
    auxilio.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        pesada = leve = auxilio[1]
    else:
        if auxilio[1] > pesada:
            pesada = auxilio[1]
        elif auxilio[1] < leve:
            leve = auxilio[1]
    pessoa.append(auxilio[:])
    auxilio.clear()
    resp = input('Quer continuar [S/N]? ').strip()[0]
    if resp in 'nN':
        break
for c in pessoa:
    if c[1] == pesada:
        pp.append(c[0])
    elif c[1] == leve:
        pl.append(c[0])
print(f'Você adicionou {len(pessoa)} pessoas')
print(f'O maior peso é de {pesada} da pessoas {pp}')
print(f'O menor peso é de {leve} das pessoas {pl}')