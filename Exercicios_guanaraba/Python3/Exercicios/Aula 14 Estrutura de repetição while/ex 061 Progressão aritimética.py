'''
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while.
'''

termo=int(input('Primeiro termo da PA: '))
razão=int(input('Insira a razão da PA: '))

print(termo,end='')

c=1
while c < 10:

    termo = termo + razão
    print('-{}'.format(termo),end='')

    c+=1