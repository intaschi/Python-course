n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
if m < 5:
    print('Você está de REPROVADO')
elif 5 < m <= 6.9:
    print('Você está de RECUPERAÇÃO')
elif m > 6.9:
    print('Você está APROVADO')