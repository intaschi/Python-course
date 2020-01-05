print('Gerador de PA:')
print('=-' * 20)
p = int(input('Primeiro termo:'))
r = int(input('Razão da PA:'))
cont = 0
while cont <= 10:
    print('{} >> '.format(p), end = '')
    p = p + r
    cont += 1
print('PAUSA')
t = 1
while t > 0:
    t = int(input('Quantos termos a mais você quer mostrar? '))
    ncont = 0
    while ncont < t:
        print('{} >> '.format(p), end='')
        p = p + r
        ncont += 1
        cont += 1
    print('PAUSA')
print('Progressão finalizada com {} termos mostrados.'.format(cont))