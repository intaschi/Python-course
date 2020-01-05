print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
c50 = c10 = c1 = 0
cont50 = cont10 = cont1 = 0
v = int(input('Que valor você quer sacar? R$ '))
while True:
    if (c50 + 50) > v:
        break
    cont50 += 1
    c50 = 50 * cont50
while True:
    if (c10 + 10) > (v - c50):
        break
    cont10 += 1
    c10 = 10 * cont10
while True:
    if (c1 + 1) > (v - c50 - c10):
        break
    cont1 += 1
    c1 = 1 * cont1
print(f'Total de {cont50} cédulas de R$ 50,00')
print(f'Total de {cont10} cédulas de R$ 10,00')
print(f'Total de {cont1} cédulas de R$ 1,00')