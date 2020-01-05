lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    '''if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)'''
    resp = input('Deseja continuar? [S/N]').strip()[0]
    if resp in 'nN':
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista total é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')