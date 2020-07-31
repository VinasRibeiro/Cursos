'''
escreva um programa que faça o computador "pensa" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.




miha solução
import random
n1=random.randrange(0,6)
numser=int(input('Insira o numero :'))

if n1 == numser:
    print('Acertou')
else:
    print('Errou')

print('Saiu o numero {} '.format(n1))
'''

#solução do curso em video

from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "Pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar

print('Processando...')
sleep(2)

if jogador == computador:
    print('Parabens! Você ganhou!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))