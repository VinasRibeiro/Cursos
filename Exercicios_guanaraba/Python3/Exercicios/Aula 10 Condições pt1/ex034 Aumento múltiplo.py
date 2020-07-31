'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento,

Para salários superiores a R$1.250,00, Calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

'''

sal = float(input('Insira o salário :'))

if sal > 1250:
    print('Seu salário aumentou 10% e foi para {}'.format(sal+((sal/100)*10)))
else:
    print('Seu salário aumentou para 15% e foi para {}'.format(sal+((sal/100)*15)))