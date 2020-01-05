f = input('Digite uma frase: ')
f.split()
fr = f.replace(' ', '')
l = len(fr)
print(fr)
inverso = ''
for c in range(l-1, -1, -1):
    print('{}'.format(fr[c]), end='')
    inverso += fr[c]
if fr == inverso:
    print('\nÉ um acrônomo')
elif fr != inverso:
    print('\nNão é um acrônomo')

f = input('Digite uma frase: ')
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    print(junto[c])


f = input('Digite uma frase: ')
f.split()
fr = f.replace(' ', '')
l = len(fr)
print(fr)
for c in range(l-1, -1, -1):
    print('{}'.format(fr[c]), end='')
if fr == fr[c]:
    print('\nÉ um acrônomo')
elif fr != fr[c]:
    print('\nNão é um acrônomo')
