'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada KM acima do limite.

'''

km=int(input('Insira a velocidade atingida: '))

if km > 80:
    print('Voce foi multado em R${}'.format(7*(km-80)))
else:
    print('Você esta respeitando o limite, parabéns')


