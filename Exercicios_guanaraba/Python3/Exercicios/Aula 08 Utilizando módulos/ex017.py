#Faça um programa que leia o comprimento de do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule
#e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Insira o seno :'))
ca = float(input('Insira o coss :'))
#Este módulo veio da biblioteca math e retorna o valor da hipotenusa
hi = hypot(co,ca)

#Esta equação faz o mesmo calculo que o módulo hypot()
#hi = (co ** 2 + ca ** 2) ** (1/2)

print('O resultado é : {}'.format(hi))
