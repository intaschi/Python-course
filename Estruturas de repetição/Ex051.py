print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
p = int(input('primeiro termo: '))
r = int(input('razão: '))
d = p + (9 * r)
for c in range(p, d + r, r):
    print(c)
for c in range(1,11):
    n = p + (c-1)*r
    print('{}'.format(n), end=' -> ')
print('ACABOU')