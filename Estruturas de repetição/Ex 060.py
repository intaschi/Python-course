n = int(input('Digite um número para calcular seu fatorial: '))
j = n
f = 1
for j in range (n, 0, -1):
    print('{}'.format(j), end='')
    print(' X ' if j > 1 else ' = ', end='')
    f = f * j
print(f)

n = int(input('Digite um número para calcular seu fatorial: '))
j = n
f = 1
while j > 0:
    print('{}'.format(j), end ='')
    print(' X ' if j > 1 else ' = ', end = '')
    f = f * j
    j = j - 1
print(f)

from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))