import random
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n4 = (input('Aluno 3: '))
n3 = (input('Aluno 4: '))
list = [n1, n2, n3, n4]
random.shuffle(list)
print('{}'.format(list))
