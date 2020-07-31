'''
Crie um programa que leia vários números inteiros pelo teclado, No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos.
O programa deve pergutnar ao usuário se ele quer ou não continuar a digitar valores.
'''

total = 0
maior = 0
menor = 0
cont = 0
escolha = 'S'

while escolha != 'N':

    n1 = int(input('Insira o numero: '))
    cont +=1
    total += n1

    if cont == 1:
        maior = n1
        menor = n1
    else:
        if  n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

    escolha = str(input('Gostaria de continuar [S:N]? ')).upper()
print('O total de numeros é {}, a média é {}, o maior é {} o menor é {}'.format(cont,total/cont,maior,menor))
