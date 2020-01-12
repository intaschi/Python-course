def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        a = str(input(msg))
        if a.isnumeric():
            valor = int(a)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor



n = LeiaInt('Digite um número: ')
print(f'O número que você digitou foi {n}')