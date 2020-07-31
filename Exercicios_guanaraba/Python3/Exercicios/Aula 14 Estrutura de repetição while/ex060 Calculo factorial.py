'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

ex:
5!=5x4x3x2x1=120

'''


n = int(input('Insira o numero: '))

fator=1

while n > 0:

    print('{} '.format(n),end='')
    print('x ' if n > 1 else' = ',end='')
    fator=fator*n

    n-=1
print(fator)


#Código do professor


# com função factorial
'''
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O factorial de {} é {}.'.format(n,f))
'''

