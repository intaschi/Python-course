print('{:-^40}'.format(' LOJA SUPER BARATÃO '))
s = 0
cont = 0
vezes = 0
while True:
    nome = input('Nome do produto: ')
    preço = float(input('Preço: R$ '))
    c = ' '
    s += preço
    vezes += 1
    if preço > 1000:
        cont =+ 1
    if vezes == 1:
        pbarato = preço
        nbarato = nome
    else:
        if preço < pbarato:
            pbarato = preço
            nbarato = nome
    while c not in 'SN':
        c = input('Quer continuar [S/N]? ').strip().upper()[0]
    if c == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi de R${s}')
print(f'Temos {cont} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi o {nbarato} que custou R${pbarato}')


