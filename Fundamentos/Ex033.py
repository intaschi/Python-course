n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
if n1 > n2 and n1<n3:
    print('O maior número é:{:.0f}'.format(n1))
if n2 > n1 and n2< n3:
    print('O maior número é: {}'.format(n2))
if n3 > n2 and n3<n1:
    print('O maior número é: {}'.format(n3))
if n1 < n2 and n3:
    print('O menor número é: {}'.format(n1))
if n2 < n2 and n3:
    print('O menor número é: {}'.format(n2))
if n3 < n2 and n1:
    print('O menor número é: {}'.format(n3))