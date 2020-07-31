'''
Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

resultado = vitorias = 0

while True:

    computador = randint(0,10)
    print(f'computador {computador}')
    pijogador = str(input('PAR ou IMPAR: ')).strip().upper()
    jogador = int(input('Insira o numero: '))

    resultado = computador + jogador


    if resultado % 2 == 0 and pijogador == 'PAR':
        print('Você ganhou')
        vitorias += 1
    else:
        if resultado % 2 != 0 and pijogador =='IMPAR':
            print('Você ganhou')
            vitorias += 1
        else:
            print(f'Você perdeu \nTotal de vitorias :{vitorias}')
            break



