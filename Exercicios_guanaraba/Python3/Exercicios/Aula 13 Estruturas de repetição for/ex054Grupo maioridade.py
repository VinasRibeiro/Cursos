'''
Crie um programa que leia o ano de nascimento de sete pessoas. No Final,
mostre quantas pessoas ainda não aintigram a maioridade
e quantas já são maiores.
'''

from datetime import date
atual = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    ano = int(input('Pessoa numero {} insira o ano de seu nascimento: '.format(c)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
    
print('{} pessoas menores, {}pessoas maiores'.format(menor,maior))

