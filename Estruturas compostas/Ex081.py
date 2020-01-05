lista = []
apareceu = False
while True:
    v = int(input('Digite um valor: '))
    if v in lista:
        print('Valor duplicado. Não adicionado')
    else:
        lista.append(v)
        print('Valor adicionado com sucesso.')
    if v == 5:
        apareceu = 'sim'
    resp = input('Deseja continuar?')
    if resp in 'nN':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if apareceu == 'sim':
    print(f'O valor 5 foi encontrado na lista!')
else:
    print(f'O valor 5 não foi encontrado na lista')
