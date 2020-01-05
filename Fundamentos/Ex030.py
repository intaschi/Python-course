n = input('Escolha um número inteiro:')
nu = len(n)
if int(n[nu - 1]) == 2 or 4 or 6 or 8 or 0:
    print('o número é par')
else:
    print('O número é impar')