from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida! Tente novamente.')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida! Tente novamente.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida! Tente novamente.')



lista = ['pedra', 'papel', 'tesoura']
import random
c = random.choice(lista).lower().strip()
p = str(input('Pedra, papel ou tesoura?')).lower().strip()
if c == p:
    print('Eu escolho {}!'.format(c.upper()))
    print('opa, parece que deu empate!')
elif (c == 'pedra' and p == 'papel') or (c == 'tesoura' and p == 'pedra') or (c == 'papel' and p == 'tesoura'):
    print('Eu escolho {}!'.format(c.upper()))
    print('VOCÊ GANHOU!')
else:
    print('Eu escolho {}!'.format(c.upper()))
    print('EU GANHEI!')

