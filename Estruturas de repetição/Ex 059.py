n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
e = int(input('Qual a sua opção? '))
while e != 5:
    if e == 1:
        s = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, s))
    elif e == 2:
        m = n1 *n2
        print('O resultado de {} X {} é {}'.format(n1, n2, m))
    elif e == 3:
        if n1 > n2:
            print('Entre {} e {}, {} é o maior número'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {}, {} é o  maior número'.format(n1, n2, n2))
    elif e == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
        e = int(input('Qual a sua opção'))
    else:
        print('Opção inválida!')
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    e = int(input('Qual a sua opção'))
print('Você saiu do programa')