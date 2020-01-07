from time import sleep

def maior(*núm):
    print('Analisando os valores passados...')
    tam = len(núm)
    maior = 0
    for c in range(0, tam):
        print(f'{núm[c]} ', end='')
        sleep(0.5)
        if c == 0:
            maior == núm[c]
        else:
            if núm[c] > maior:
                maior = núm[c]
    print()
    print(f'Você forneceu {tam} valores e o maior foi {maior}')

maior(0, 9, 3, 5, 1, 7)
