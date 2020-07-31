'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status,
de acordo com a tabela abaixo:
-Abaixo de 18.5:Abaixo do peso
-Entre 18.5 e 25:PEso ideal
-25 até 30:Sobrepeso
-30 até 40:Obesidade
-Acima de 40:
Obesidade mórbida
'''
peso = float(input('Coloque seu peso :'))
altura = float(input('Coloque sua altura :'))

numero = peso / (altura ** 2)

if numero < 18.5:
    print('Você esta abaixo do peso')
elif numero <= 25:
    print('Você esta no peso ideal')
elif numero <= 30:
    print('Você esta com sobre peso')
elif numero <= 40:
    print('Você esta com obesidade')
elif numero > 40:
    print('Você esta com Obesidade mórbida')