d = float(input('Qual a distância, em km, da sua viagem?'))
if d <= 200:
    print('A passagem fica R${:.2f}'.format(d*0.5))
else:
    print('A passagem fica R${:.2f}'.format(d*0.45))