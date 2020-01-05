import random
cont = 0
print('Acabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')
e = random.randint(1, 10)
acertou = False
while not acertou:
    n = int(input('Qual é o seu palpite?'))
    cont += 1
    if n == e:
        acertou = True
    else:
        if n > e:
            print('Menos, tente novamente!')
        elif e > n:
            print('Mais, tente novamente!')
print('Acertou com {} tentativas. Parabéns!'.format(cont))

import random
cont = 0
print('Acabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')
e = random.randint(1, 10)
n = int(input('Qual é o seu palpite?'))
while n != e:
    print('Esse não é o número. O certo seria {}. Tente mais uma vez!'.format(e))
    e = random.randint(1, 10)
    n = int(input('Qual é o seu palpite?'))
    cont += 1
print('ACERTOU com {} tentativas'.format(cont))

