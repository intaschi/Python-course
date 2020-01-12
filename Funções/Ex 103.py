def jogador(nome = 'desconhecido', gols = 0):
    print(f'O jogador {nome} fez {gols} gols')

n = input(str('Nome do jogador: '))
g = input('Quantos gols o jogador fez? ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    jogador(gols=g)
else:
    jogador(n, g)