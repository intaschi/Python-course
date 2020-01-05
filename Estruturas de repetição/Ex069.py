print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
cont = 0
homem = 0
mulher = 0
while True:
    i = int(input('IDADE: '))
    s = input('SEXO [F/M]: ').strip().upper()
    while s not in 'FM':
        print('Valor inválido.')
        s = input('SEXO [F/M]: ').strip().upper()
    print('-' * 20)
    c = input('Quer continuar? [S/N]').strip().upper()[0]
    if i > 18:
        cont += 1
    if s == 'M':
        homem += 1
    if s == 'F' and i < 20:
        mulher += 1
    while c not in 'SN':
        c = input('Quer continuar? [S/N]').strip().upper()[0]
    if c == 'N':
        print(f'Total de pessoas com mais de 18 anos: {cont}')
        print(f'Total de homens cadastrados: {homem}')
        print(f'Total de mulheres com menos de 20 anos: {mulher}')
        break