sexo = input('Qual o seu sexo? ').strip().lower()
while sexo not in 'mf':
    print('Inválido, digite novamente!')
    sexo = input('Qual o seu sexo? ').strip().lower()
print('Valor registrado com sucesso')