v = int(input('Velocidade do carro: '))
if v > 80:
    print('Você ultrapassou a velocidade máxima permitida e deverá pagar uma multa no valor de R${:.2f} '.format(float(v-80)*7))