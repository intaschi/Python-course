lisa = [[], []]
for c in range(0, 8):
    valor = int(input(f'Digite o {c+1}° valor'))
    if valor % 2 == 0:
        lisa[0].append(valor)
    else:
        lisa[1].append(valor)
print(lisa[0])