from random import randint
v = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Os valores sorteados foram', end = '')
for c in v:
    print(f'{c}')
print(f'Os valores sorteados foram {v}')
print(f'O maior valor sorteado foi {max(v)}')
print(f'O menos valor sorteado foi {min(v)}')




n1 = randint(1, 100)
n2 = randint(1, 100)
n3 = randint(1, 100)
n4 = randint(1, 100)
v = (n1, n2, n3, n4)
print(v)
maior = menor = n1
for c in v:
    if c == n1:
        maior == menor == n1
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f'O maior valor é {maior}')
print(f'O menos valor é {menor}')
