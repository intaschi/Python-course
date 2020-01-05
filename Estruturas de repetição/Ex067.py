m = 0
cont = 0
while True:
    v = int(input('Quer ver a tabuada de qual valor? '))
    if v < 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        m = v * cont
        print(f'{v} x {cont} = {m}')
    print('-'*20)
