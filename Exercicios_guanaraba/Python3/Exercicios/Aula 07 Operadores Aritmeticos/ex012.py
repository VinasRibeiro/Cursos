#ex012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod=float(input('Insira o preço do produto :'))
desc=prod-(5*prod/100)

print('Com desconto o produto saiu a {:.2f}'.format(desc))