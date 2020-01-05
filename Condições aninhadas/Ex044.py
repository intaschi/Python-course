print('{:=^40}'.format(' LOJAS CAROL '))
print('''Formas de pagamento:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] Parcelado em 2x''')

preço = float(input('Qual o preço do produto? '))
condição = str(input('Você vai pagar à vista ou parcelado? '))
if condição.lower().strip() == 'à vista' or condição.lower().strip() == 'a vista':
    condição2 = str(input('Dinheiro, cheque ou cartão? '))
    if condição2.lower().strip() == 'dinheiro' or condição2.lower().strip() == 'cheque':
        print('O valor total fica R${}'.format(preço - (0.1*preço)))
    elif condição2.lower().strip() == 'cartão':
        print('O valor total fica R$ {}'.format(preço - 0.05*preço))
elif condição.lower().strip() == 'parcelado':
    condição2 = str(input('Quantas parcelas? '))
    if condição2 <=2:
        print('O valor total fica R${}'.format(preço))
    elif condição2 > 2:
        print('O valor total fica R${}'.format(preço + (0.2*preço)))