lista = []
cont = 0
while True:
    v = int(input('Digite um valor: '))
    if v in lista:
        print('Valor duplicado. Não adicionado.')
    if v not in lista:
        if cont == 0 or v > lista[len(lista)-1]:
            lista.append(v)
            print('Valor adicionado ao final da lista')
        else:
            pos = 0
            while pos < len(lista):
                if v <= lista[pos]:
                    lista.insert(pos, v)
                    break
                pos += 1
            print(f'Valor adicionado na posição {pos}')
    resp = input('Deseja continuar?').strip()[0]
    if resp in 'Nn':
        break
    cont += 1
print(f'Você digitou os números {lista}')



'''lista = []
posição = 0
cont = 0
while True:
    v = int(input('Digite um valor: '))
    if v in lista:
        print('Valor duplicado. Não adiconado.')
    if v not in lista:
        if cont == 0:
            lista.insert(v, 0)
            print(f'O valor {v} foi adicionado ao final da lista')
        else:
            if v > lista[len(lista) - 1]:
                lista.insert(v, len(lista) - 1)
                print(f'O valor {v} foi adicionado ao final da lista')
            elif v < lista[0]:
                lista.insert(v, 0)
                print(f'O valor {v} foi adicionado ao começo da lista')
            else:
                while True:
                    if v > lista[posição] and v < lista[posição + 1]:
                        lista.insert(v, posição)
                        break
                    else:
                        posição += 1
                print(f'Você adicionou o valor {v} na posição {posição}')
    cont += 1
    resp = input('Quer continuar?').strip().upper()[0]
    if resp in 'N':
        break
print(f'Você digitou os valores {lista}')'''