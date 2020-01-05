ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = int(input('Digite um número entre 0 e 10:'))
while True:
    if 0 < n < 10:
        print(f'Você digitou {ne[n]}')
        break
    else:
        n = int(input('Digite um número entre 0 e 10:'))