print('-'*40)
print('          JOGO NA MEGA SENA          ')
print('-'*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-+'*3, f'SORTEANDO {(jogos)} JOGOS', '-+'*3,)
import random
from time import sleep
lista = []
aux = []
for b in range(0, jogos):
    while len(aux) < 6:
        n = random.randint(0, 60)
        if n not in aux and n not in lista:
            aux.append(n)
    aux.sort()
    lista.append(aux[:])
    aux.clear()
for c in range(0, jogos):
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(1)


