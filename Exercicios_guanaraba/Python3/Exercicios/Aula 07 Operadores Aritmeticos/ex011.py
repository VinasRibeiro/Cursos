#ex011
#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#nescessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrado.

larg=float(input('Insira a largura : '))
alt=float(input('Insira a altura : '))
tinta=(larg*alt)/2
print('A quantidade de tinta nescessaria é: {:.3f}'.format(tinta))
