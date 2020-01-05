n = s = cont = 0
n = int(input('Digite um número: '))
while n != 999:
   s += n
   n = int(input('Digite um número: '))
print('A soma entre os números é {}'.format(s))