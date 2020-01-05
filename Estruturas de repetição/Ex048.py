s = 0
cont = 0
for n in range(0, 501):
    if n % 2 == 1 and n % 3 == 0:
        cont = cont + 1
        s += n
print('A soma de todos os {}  resulta da soma {}'.format(cont, s))
#for n in range(0, 500, 3):
 #   if n % 2 == 1:
  #      print(n, end = ' ')