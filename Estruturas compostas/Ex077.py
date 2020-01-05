t = ('palavra', 'pao', 'caderno')
for palavra in t:
    print(f'\nNa palavra {palavra.upper()} temos: ', end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')

'''for c in range(0, len(t)):
    print(f'\nNa palavra {t[c].upper()} temos: ', end = '')
    if 'a' in t[c]:
        print(f'a ', end = '')
    if 'e' in t[c]:
        print(f'e ', end='')
    if 'i' in t[c]:
        print(f'i ', end='')
    if 'o' in t[c]:
        print(f'o ', end='')
    if 'u' in t[c]:
        print('u')'''

