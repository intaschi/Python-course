num = [2, 5, 9, 1]
'''nume = list(2, 5, 9, 1)'''
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print(f'Não achei o número {num}')
print(num)
print(f'Essa lista tem {len(num)} elementos')

num = []
num.append(1)
num.append(2)
num.append(3)
for cont in range(0, 5):
    num.append(int(input('Digite um valor:')))
for v in num:
    print(f'{v}...')

for c, v in enumerate(num):
    print(f'na posição {c}, encontrei o valor {v}...')

a = [1, 2, 3, 4]
# a = b > tudo que eu alterar em uma lista, altera também na outra
b = a[:]
b[2] = 8
