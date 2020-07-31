'''
Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maioe valor que estão na tupla.

'''
from random import randint

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))


print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


#Tbm pode ser usado a forma simples
#Nesta forma ele mostra todos os numeros gerados
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Eu sorteei o valor {n}')