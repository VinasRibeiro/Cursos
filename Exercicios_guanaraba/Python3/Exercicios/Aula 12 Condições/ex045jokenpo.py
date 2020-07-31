'''
Crie um programa que faça o computador jogar jokenpo com você.

'''
import emoji
from random import randint
usuario = int(input('as opções são \n1: Pedra \n2: Tesoura \n3: Papel\n'))
computador = randint(1,3)
print(computador)

if usuario == 1 and computador ==2:
    print (emoji.emojize('Você escolheu :fist: e o computador escolheu :v:',use_aliases=True))
    print ('Você ganhou')
elif usuario == 2 and computador == 3:
    print(emoji.emojize('Você escolheu :v: e o computador escolheu :raised_hand:',use_aliases=True))
    print('Você ganhou')
elif usuario == 3 and computador == 1:
    print(emoji.emojize('Você escolheu :raised_hand: e o computador escolheu :fist:',use_aliases=True))
    print('Você ganhou')
elif usuario == computador:
    print('Deu empate')
else:
    if computador == 1 and usuario == 2:
        print('Você perdeu')
        print(emoji.emojize('Você escolheu :v: e o computador escolheu :fist:', use_aliases=True))
    elif computador == 2 and usuario == 3:
        print('Você perdeu')
        print(emoji.emojize('Você escolheu :raised_hand: e o computador escolheu :v:', use_aliases=True))
    elif computador == 3 and usuario == 1:
        print('Você perdeu')
        print(emoji.emojize('Você escolheu :fist: e o computador escolheu :raised_hand:', use_aliases=True))

