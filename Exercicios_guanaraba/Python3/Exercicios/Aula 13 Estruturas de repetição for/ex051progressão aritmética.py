'''
PA = progressão aritimética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.


term1 = int(input('Insira o 1 termo: '))
razão = int(input('Insira a razão: '))

for c in range(0,10):
    print(term1)
    term1 += razão
'''

#Código do professor

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):

    print('{} '.format(c), end='- ')

print('ACABOU')