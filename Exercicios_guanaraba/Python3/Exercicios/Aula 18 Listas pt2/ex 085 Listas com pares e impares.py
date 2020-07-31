'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.

'''
lista = [[],[]]
n = 0
for c in range(1,8):

    n = int(input('n :'))

    if n %2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)


lista[0].sort()
lista[1].sort()
print(lista)
print(f'Impares {lista[1]}')
print(f'Pares {lista[0]}')

