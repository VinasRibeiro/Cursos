'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a area do terreno.
'''

def area(a, b):
    m = a * b
    print(f'O terreno tem {m} M²')




comp = float(input('Comprimento: '))
larg = float(input('Largura: '))
area(larg, comp)



