n = int(input('Digite um número:'))
d = input('Deseja continuar? [S/N]').strip().upper()
cont = 1
soma = n
maior = n
menor = n
m = n
while d not in 'nN':
    n = int(input('Digite um número:'))
    cont += 1
    soma += n
    m = soma/cont
    if n > maior:
        maior = n
    menor = n
    if n < menor:
        menor = n
    d = input('Deseja continuar? [S/N]').strip().upper()
print('Você digitou {} números e a média entre eles foi {}'.format(cont, m))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))