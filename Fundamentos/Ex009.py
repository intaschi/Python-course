d = int(input('Quantos dias o carro foi alugado?'))
km = int(input('Quantos km foram rodados?'))
pago = (60*d) + (0.15*km)
print('O valor total a ser pago é {}'.format(pago))

t = int(input('Qual a temperatura em C°?'))
f = 32 + ((t*9)/5)
print('essa temperatura em Fahrenheit é igual a {:.0f}'.format(f))

n = int(input('Digite um número para ver a sua tabuada:'))
print('--------------')
print('{} x 1 = {}'.format(n,(n*1)))
print('{} x 2 = {}'.format(n,(n*2)))
print('{} x 3 = {}'.format(n,(n*3)))
print('{} x 4 = {}'.format(n,(n*4)))
print('{} x 5 = {}'.format(n,(n*5)))
print('{} x 6 = {}'.format(n,(n*6)))
print('{} x 7 = {}'.format(n,(n*7)))
print('{} x 8 = {}'.format(n,(n*8)))
print('{} x 9 = {}'.format(n,(n*9)))
print('{} x 10 = {}'.format(n,(n*10)))
print('--------------')


