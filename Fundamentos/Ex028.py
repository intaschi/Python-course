import random
comp = random.randint(0,5)
n = input()
n = [0,1,2,3,4,5]
import random
e = random.choice(n)
p = input('Qual número eu estou pensando, de 0 a 5? ')
if p == e:
    print('Parabéns, você acertou!')
else:
    print('Esse não é o número, o certo seria {}'.format(e))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média é {:.1f}'.format(m))
if m >= 6:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado')

nome = str(input('Qual o seu nome?'))
if nome.strip().lower() == 'renata':
    print('Que nome lindo você tem!')
print('Bom dia, {}'.format(nome))

