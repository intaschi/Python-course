ano = int(input('Ano de nascimento: '))
import datetime
n = datetime.date.today().year
idade = n - ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')