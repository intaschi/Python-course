matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [ {l}, {c} ]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print( )
listapar = []
somapar = 0
somacoluna = 0
listacoluna = []
mvalor = 0
for c in range(0, len(matriz)):
    for b in range(0, 3):
        if matriz[c][b] % 2 == 0:
            somapar += matriz[c][b]
            listapar.append(matriz[c][b])
        if b == 2:
            somacoluna += matriz[c][b]
            listacoluna.append(matriz[c][b])
        if c == 1 and b == 0:
            mvalor = matriz[c][b]
        else:
            if c == 1 and matriz[c][b] > mvalor:
                mvalor = matriz[c][b]
print(f'A lista de números pares é: {listapar}')
print(somapar)
print(listacoluna)
print(somacoluna)
print(f'O maior valor da segunda linha é: {mvalor}')
