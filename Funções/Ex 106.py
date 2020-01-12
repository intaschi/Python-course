def ajuda(foub):
    help(foub)

def titulo(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
