o = float(input('comprimento do cateto oposto: '))
a = float(input('comprimento do cateto adjacente: '))
import math
h = math.sqrt(o**2+a**2)
hi = math.hypot(o,a)
print('A hipotenusa vai ser {}'.format(math.hypot(o,a)))