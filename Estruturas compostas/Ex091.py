from random import randint
from time import sleep
from operator import itemgetter
valores = {}
ranking = ()
print('Valores sorteados')
valores['Jogador1'] = randint(1,6)
valores['Jogador2'] = randint(1,6)
valores['Jogador3'] = randint(1,6)
valores['Jogador4'] = randint(1,6)
for k, v in valores.items():
    print(f'O {k} tirou {v} nos dados.')
    sleep(0.5)
print('=-'*30)
print(f'{" RANKING DOS JOGADORES ":=^30}')
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k + 1} lugar: O {v[0]} tirou {v[1]}')