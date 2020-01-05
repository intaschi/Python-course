hvelho = ''
ivelho = 0
mulheres = 0
sidade = 0
for c in range(1, 4):
    print('---- {}° PESSOA ----'.format(c))
    n = input('NOME: ')
    i = int(input('IDADE: '))
    s = input('SEXO [M/F]: ').strip().lower()
    sidade = sidade + i
    if c == 1 and s == 'm':
        hvelho = n
        ivelho = i
    if s == 'm' and i > ivelho:
            hvelho = n
            ivelho = i

    if i < 20 and s == 'f':
        mulheres = mulheres + 1
m = (sidade)/3
print('A média das idades é {}'.format(m))
print('O homem mais velho chama {} e tem {} anos'.format(hvelho, ivelho))
print('Temos {} mulheres com menos de 20 anos'.format(mulheres))