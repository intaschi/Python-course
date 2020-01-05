import random
s = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*20)
venceu = 0
while True:
    jogador = int(input('Digite um valor: '))
    e = input('Par ou Ímpar [P/I]?').strip().upper()[0]
    while e not in 'PI':
        e = input('Par ou Ímpar [P/I]?').strip().upper()[0]
    comp = random.randint(1, 10)
    s = jogador + comp
    if e == 'P' and s % 2 == 0:
        print(f'Você escolheu {jogador} e o computador escolheu {comp}. Total de {s} DEU PAR.\nVOCÊ VENCEU!')
        venceu += 1
    elif e == 'P' and s % 2 == 1:
        print(f'Você escolheu {jogador} e o computador escolheu {comp}. Total de {s} DEU ÍMPAR.\nVOCÊ PERDEU!')
        print(f'GAME OVER!\nVocê venceu {venceu} vezes.')
        break
    elif e == 'I' and s % 2 == 0:
        print(f'Você escolheu {jogador} e o computador escolheu {comp}. Total de {s} DEU PAR.\nVOCÊ PERDEU!')
        print(f'GAME OVER!\nVocê venceu {venceu} vezes.')
        break
    elif e == 'I' and s % 2 == 1:
         print(f'Você escolheu {jogador} e o computador escolheu {comp}. Total de {s} DEU ÍMPAR.\nVOCÊ VENCEU!')
         venceu += 1
    print('Vamos jogar novamente...')