from operator import itemgetter
dados = {}
gols = []
jogadores = []
total = 0
while True:
    dados.clear()
    gols.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        total += gols[c]
    dados['gols'] = gols[:]
    dados['total'] = total
    jogadores.append(dados.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO. Responda S ou N.')
    if resp == 'N':
        break
print('=-' * 30)
print(f'{"cod. "}', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for c in range(0, len(jogadores)):
    print(f'{c:<4} ', end='')
    for d in jogadores[c].values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
while True:
    n = int(input('Mostrar os dados de qual jogador (999 para parar)? '))
    if n == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR: {jogadores[n]["nome"]}')
    for k, v in enumerate(jogadores[n]['gols']):
        print(f'No jogo {k} fez {v} gols.')
print('='*40)
print('<<< VOLTE SEMPRE >>>')

