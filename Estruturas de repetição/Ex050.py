soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números e a soma é {}'.format(cont, soma))



n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n4 = int(input('Segundo número: '))
n5 = int(input('Quinto número: '))
n6 = int(input('Sexto número: '))
lista = [n1, n2, n3, n4, n5, n6]
s = 0
for c in range(0, 6):
    n = lista[c]
    if n % 2 == 0:
        s = s + n
print(s)

#if n1 % 2 == 1:
 #   n1 = 0
#if n2 % 2 == 1:
 #   n2 = 0
#s = (n1 + n2 + n3 + n4 + n5 + n6)
#print(s)