dados = {}
gols = []
total = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    total += gols[c]
dados['gols'] = gols[:]
dados['total'] = total
print('=-' * 30)
print(dados)
print('=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    > Na partida {c} fez {dados["gols"][c]} gols.')
print(f'Fez um total de {total} gols.')
