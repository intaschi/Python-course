s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))
if s1 < s2 +s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 > abs(s2 - s3) and s2 > abs(s1 - s3) and s3 > abs(s1 - s2):
    print('Esses segmentos PODEM formar um triângulo')
    if s1 == s2 == s3:
        print('Esse triângulo é equilátero!')
    if s1 == s2 or s2 == s3 or s1 == s3:
        print('Esse triângulo é isóceles!')
    else:
        print('Esse triângulo é escaleno!')
else:
    print('Esses segmentos NÃO PODEM formar um triângulo')
