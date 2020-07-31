'''
Refaça o desafio 009. mostrando a tabuada de um número que p usuário
escolher, só que agora utilizando um laço for.

'''

'''
n1=int(input('Insira o numero da tabuada: '))
cont = 0
print('-'*12)
for c in range(1,11):
    print(' {} X {:2} = {}'.format(n1,cont,n1*c))
    cont = cont + 1
'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))