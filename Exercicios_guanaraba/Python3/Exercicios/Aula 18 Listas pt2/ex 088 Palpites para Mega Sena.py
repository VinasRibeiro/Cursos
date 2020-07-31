'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.


from random import randint

sorteio = list()
cartela = list()
njogos = 0


njogos = int(input('Quantos jogos vc vai fazer?: '))


for c in range(0,njogos):

    for v in range(0,6):

        cartela.append(randint(1,60))


    sorteio.append(cartela[:])
    cartela.clear()
    print(f'jogo {c+1} = {sorteio[c]}')
'''
#Versão do professor sem repetição

from random import randint
lista = list()
cont = 0
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break

# essa é a estrutura para não repetir os numeros
#Mas fiquei com preguiça de copiar









