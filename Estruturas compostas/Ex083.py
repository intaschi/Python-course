expressão = input('Digite uma expressão matemática:')
lista = []
for c in expressão:
    if c == '(':
        lista.append(1)
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(1)
            break
if len(lista) == 0:
    print('A expressão é valida')
else:
    print('A sua expressão é inválida.')
