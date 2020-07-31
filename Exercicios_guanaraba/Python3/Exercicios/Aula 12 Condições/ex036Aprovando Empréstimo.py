'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa.

O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado.
'''

salario = float(input('Quanto você ganha por mês?: '))
casa = float(input('Qual o valor da casa?:'))
prazo = int(input('Quantos anos de financiamento?:'))

prestação = casa / (prazo*12)

if prestação > salario/100*30:
    print('\033[0;31;0mSeu crédito não foi aprovado\033[m')
else:
    print('\033[0;32;0mSeu crédito foi aprovado\033[m')
'''
a função end='' faz com que a linha não quebre para outra linha 
'''
print('salario é {}'.format(salario))
print('O valor da prestação é {:.2f}'.format(prestação))

