peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso/(altura ** 2)
if IMC < 18.5:
    print('Você está abaixo do peso')
elif 18.5 < IMC < 25:
    print('Você está no peso ideal')
elif 25 < IMC < 30:
    print('Você está com sobrepeso')
elif 30 < IMC < 40:
    print('Você está obeso')
elif IMC > 40:
    print('Obesidade móbida')
