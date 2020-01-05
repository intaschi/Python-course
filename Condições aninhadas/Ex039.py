i = int(input('Qual o seu ano de nascimento?'))
import datetime
ano = datetime.date.today().year
if (ano - i) >= 18:
    print('Você deve se alistar!')
if ano - i <18:
    print('Você ainda vai se alistar!')