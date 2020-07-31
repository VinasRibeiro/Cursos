'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os e uma tupla. No final mostre:

A)Quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C)Quais foram os números pares.

'''
#quando os parenteses são usados eles convertem as variaveis em tuplas

num = (int(input('n1: ')),
       int(input('n2: ')),
       int(input('n3: ')),
       int(input('n4: ')))
print(f'Voce digitou {num}')
print(f'O numero 9 aparece {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1} posição')
else:
    print('O numero 3 não foi encontrado')

for c in num:
    if (c % 2) == 0:
        print(c)
