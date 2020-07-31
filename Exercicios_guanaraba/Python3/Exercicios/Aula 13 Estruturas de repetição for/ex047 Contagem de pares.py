'''
Cire um programa que mostre na tela os numeros pares que estão no
intervalo entre 1 e 500.

'''


print('Os numeros pares são')


'''
for c in range(1,51):
    if c%2 == 0:
        print('{}'.format(c))
'''

#Código do professor
#o importante é deixar o laço fazer a dedução usando o numero de pulas no numero final.
for n in range(2,51,2):
    print(n)
print('Acabou')