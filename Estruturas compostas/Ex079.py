v = []
while True:
    n = int(input('Digite um valor:'))
    if n in v:
        print('Valor duplicado... não adicionado.')
    else:
        print('Valor adicionado com sucesso.')
        v.append(n)
    resp = input('Quer continuar? [S/N]').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if 'N' in resp:
        break
print(f'Os valores digitados foram {v}')
