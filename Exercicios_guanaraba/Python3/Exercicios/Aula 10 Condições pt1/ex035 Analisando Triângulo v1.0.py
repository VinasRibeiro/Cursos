'''
Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.
ex
r1
r2
r3

'''

r1 = float(input('Insira a reta 1: '))
r2 = float(input('Insira a reta 2: '))
r3 = float(input('Insira a reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('O triangulo existe')
else:
    print('O triangulo não é possível')
