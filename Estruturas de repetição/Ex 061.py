print('Gerador de PA:')
print('=-' * 20)
p = int(input('Primeiro termo:'))
r = int(input('Razão da PA:'))
cont = 0
while cont < 10:
    print('{} >> '.format(p), end = '')
    p = p + r
    cont += 1
print('FIM')