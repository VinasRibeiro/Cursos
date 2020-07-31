'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parado.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(Desconsiderando flag).


n1 = 0
soma = 0
cont = 0

while n1 != 999:

    if n1 != 999:
        n1=int(input('Digite o numero: '))

    if n1 != 999:
        cont += 1
        soma += n1



print('{} vezes e {} total'.format(cont,soma))
print('FIM')
'''

num = cont = soma = 0
#primeira entrada de dados
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
#Segunda entrada de dados
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} a soma é {}'.format(cont,soma))

'''
Para finalizar o loop, tem que digitar 999, e para isso 
acontecer é preciso colocar duas entradas de dados pelo teclado.

'''




