import time
def contagem(a, b, c):
    if b < a and c>0:
        for c in range(a , b-1, -c):
            print(f'{c} ', end='')
            time.sleep(0.5)
        print('FIM')
    if b < a and c<0:
        for c in range(a , b-1, c):
            print(f'{c} ', end='')
            time.sleep(0.5)
        print('FIM')
    if b > a:
        for c in range(a , b+1, c):
            print(f'{c} ', end='')
            time.sleep(0.5)
        print('FIM')


#programa principal
print('Contagem de 1 até 10, de 1 em 1')
contagem(1, 10, 1)
print('='*20)
print('Contagem de 10 até 0 de 2 em 2')
contagem(10, 0, 2)
print('=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Final: '))
c = int(input('Passo: '))
contagem(a, b, c)
