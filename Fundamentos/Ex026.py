frase = input('Digite uma frase: ').lower().strip()
print('Na sua frase existem {} letras a'.format(frase.count('a')))
print('Na sua frase, o primeiro a aparece na posição {}'.format(frase.find('a')))
print('O último a aparece na posição {}'.format(frase.rfind('a')))