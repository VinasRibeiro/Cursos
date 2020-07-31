#ex013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal=float(input('Insira o salário do funcionário : '))
porc=float(input('Insira a porcentagem de aumento : '))
aum=sal+((sal/100)*porc)
print('O salario ficou em : {}'.format(aum))
