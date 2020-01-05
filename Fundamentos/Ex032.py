ano = int(input('Digite o ano aqui: '))
r = ano % 4
t = ano % 100
y = ano % 400
import datetime
print(datetime.date.today().year)
if r == 0 and t != 0 and y == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')