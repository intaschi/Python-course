t = (int(input('Valor:')), int(input('Valor:')), int(input('Valor:')), int(input('Valor:')))
print(f'Você digitou os valores \n{t}')
print(f'O número 9 apareceu {t.count(9)}')
if 3 in t:
    print(f'O número 3 aparece primeiro na {t.index(3)}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'os números pares são:', end = '')
for c in t:
    if c % 2 == 0:
        print(f'{c}', end = '')


'''for c in range(1,5):
    if c == 1:
        n1 = int(input('Valor:'))
    if c == 2:
        n2 = int(input('Valor:'))
    if c == 3:
        n3 = int(input('Valor:'))
    if c == 4:
        n4 = int(input('Valor:'))
cont9 = 0
contpar = 0
cont3 = 0
t = (n1, n2, n3, n4)
for c in t:
    if c == 9:
        cont9 += 1
    if c % 2 == 0:
        contpar += 1
    if c == 3:
        cont3 += 1
print(f'Temos {cont9} números 9')
if cont3 == 0:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O primeiro número 3 aparece na posição {(t.index(3)) + 1}')
print(f'Temos {contpar} números par')'''

