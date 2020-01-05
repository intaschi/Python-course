valor = float(input('Qual o valor da sua casa? '))
s = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você vai pagar?'))
p = valor/(anos*12)
if p > 0.3*s:
    print('O seu empréstimo foi negado!')
else:
    print('O seu empréstimo foi aprovado!')