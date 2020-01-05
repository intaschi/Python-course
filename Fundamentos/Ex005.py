s = int(input('Qual o valor do seu salário?'))
print('Com aumento de 15% o seu salário passará a ser {}'.format(s+s*0.15))
p = float(input('Qual o preço deste produto?'))
print('O preço deste produto é {},  mas com desconto de 5% fica por {}'.format(p,p-(0.05*p)))

h = float(input('Qual a altura dessa parede?'))
l = float(input('Qual a largura dessa parede?'))
print("Essa parede tem {:20} de área, e é preciso de {} litros de tinta para pinta-la".format(h*l,(h*l)/2))

R = float(input('Quantos reais você tem na sua carteira?'))
print('Com {} reais você consegue comprar {} dólares'.format(R,R/3.27))

n3 = int(input('Escreva aqui um número inteiro:'))
n4 = n3 * 1
n5 = n3 * 2
n6 = n3 * 3
print('A tabuada desse número é {}, {}, {}'.format(n4, n5, n6))

m = int(input('Escreva aqui um valor em metros'))
cm = m * 100
mm = m * 1000
print('{} m equivalem a {} cm ou a {} mm'.format(m,cm,mm))


n1 = float(input('Qual a sua nota na primeira prova?'))
n2 = float(input('Qual a sua nota na segunda prova?'))
print('A sua média final é de {}'.format((n1+n2)/2))


n = int(input('Escolha um número'))
a = n - 1
s = n + 1
print('O antecessor de {} é {} e o sucessor é {}'.format(n,a,s))

b = int(input('Escolha outro número'))
d = b + b
t = b + b + b
r = b ** 0.5
f = b ** (1/2)
print('o dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(b, d, t, r))
print(f)
