pmaior = 0
pmenor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if p == 1:
        pmaior = p
        pmenor = p
    else:
        if p > pmaior:
            pmaior = p
        if p < pmenor:
            pmenor = p
print(pmaior)
print(pmenor)
