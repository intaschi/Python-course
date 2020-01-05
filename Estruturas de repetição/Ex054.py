import datetime
s = 0
countmaior = 0
countmenor = 0
for c in range(1, 8):
    n = int(input('Digite aqui a {}° idade'.format(c)))
    if datetime.date.today().year - n >= 18:
        countmaior = countmaior + 1
    if datetime.date.today().year - n < 18:
        countmenor = countmenor + 1
print('Messe grupo temos {} mais velhas e {} mais novas'.format(countmaior, countmenor))

count = 0
i1 = int(input('Digite a idade do 1° jogador:'))
if i1 > 18:
        count = count + 1
i2 = int(input('Digite a idade do 2° jogador:'))
if i2 > 18:
    count = count + 1
i3 = int(input('Digite a idade do 3° jogador:'))
if i3 > 18:
    count = count + 1
print(count)


