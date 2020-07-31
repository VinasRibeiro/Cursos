'''
Melhore o jogo do desafio 028 onde o "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,mostrando no final
quanto palpites foram necessários para vencer.


from random import randint

computador = randint(0,5)

jogador = 9
c = 0
while jogador != computador:
    c += 1
    jogador = int(input('Insira um numero: '))

    if jogador == computador:
        print('Você ganhou')
        print('Você tentou {} vezes'.format(c))
    else:

        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
'''

#código do professor
from random import randint
computador = randint(0,10)

print('PEnsei em um nuemro entre 0 e 10.')

acertou = False
palpite = 0
while not acertou:

    jogador = int(input('Qual é o numero? '))
    palpite += 1
    if jogador == computador:
        acertou = True
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} palpites'.format(palpite))



