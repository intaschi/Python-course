lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([nome, [nota1, nota2]])
    resp = input('Quer continuar [S/N]? ')
    if resp in 'nN':
        break
print('=-' * 30)
print(f'{"No.":<10}{"NOME":<10}{"MÉIDA":>10}')
print('-' * 30)
for i, v in enumerate(lista):
    print(f'{i:<10}{v[0]:<10}{(v[1][0] + v[1][1])/2:>10}')
print('=-' * 30)
while True:
    aluno = int(input('Mostrar notas de quais alunos [999 para interromper]: '))
    if aluno == 999:
        break
    else:
        print(f'As notas de {lista[aluno][0]} são {lista[aluno][1]}')
print('>>> VOLTE SEMPRE! <<<')

