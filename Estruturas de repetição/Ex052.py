n = int(input('Digite um número:'))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
print('Esse número é divisível {} vezes'.format(cont))
if cont == 2:
   print('É um número PRIMO')
if cont > 2:
   print('{} NÃO é um número PRIMO'.format(n))