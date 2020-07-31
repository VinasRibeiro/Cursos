'''
Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artificil.
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep
import emoji


print('Vai começar a contagem')
sleep(2)
#o numero negativo -1 da ultima casa da contagem vai mostrar o 0 no final
for c in range(10,-1,-1):
    print('{}'.format(c))
    sleep(1)
print(emoji.emojize('Feliz ano novo :fireworks:',use_aliases=True))