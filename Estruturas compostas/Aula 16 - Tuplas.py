lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0, len(lanche)):
    print(cont)
    print(lanche[cont])

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
len(c)
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))

del(lanche)

pessoa = ('Carol', 39, 23.48)