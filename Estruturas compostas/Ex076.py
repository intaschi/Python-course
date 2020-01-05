t = ('pão', 1.2, 'castanha', 23, 'Água', 2.50, 'maça', 2.00)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
b = 0
n = len(t)
while True:
    print(f'{t[b]:.<20}................. R$ {t[b+1]:>10.2f}')
    b = b + 2
    if b >= n:
        break
for c in range (0, len(t)):
    if c % 2 == 0:
        print(f'{t[c]:.<20}', end = '')
    else:
        print(f'{t[c]:>10.2f}')


