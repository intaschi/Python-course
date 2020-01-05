num = []
for c in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print(num)
nmaior = nmenor = 0
for cont in range(0, len(num)):
    if cont == 0:
        nmaior = nmenor = num[cont]
    else:
       if num[cont] > nmaior:
            nmaior = num[cont]
       elif num[cont] < nmenor:
            nmenor = num[cont]
print(f'O maior valor é {nmaior} e está nas posições: ', end = '')
for pos, n in enumerate(num):
    if nmaior == n:
        print(f'{pos}... ', end = '')
print(f'\nO menor valor é {nmenor} e está nas posições: ', end = '')
for pos, n, in enumerate(num):
    if nmenor == n:
        print(f'{pos}... ', end = '')

