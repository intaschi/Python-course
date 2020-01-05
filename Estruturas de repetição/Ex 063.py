print('-'*10)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*10)
n = int(input('Quantos termos você quer mostrar?'))
p = 0
a1 = 0
a2 = 1
cont = 0
while cont <= n:
    print('{} >> '.format(p), end='')
    p = a1 + a2
    a1 = a2
    a2 = p
    cont += 1
print('FIM')
