'''
Aprimore o desafio anterior, mostrando no final:

A)A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha.

'''


lista = [[],[],[]]
n = 0
partot = 0
tot3 = 0
maximo = 0

for c in range(0,3):
    for v in range(0,3):
        n = int(input(f'Digite o numero para [{c},{v}]'))
        lista[c].append(n)


for c in range(0,3):
    tot3 += lista[c][2]
    print()
    for v in range(0,3):
        print(f'[{lista[c][v]:^5}]', end='')

        if lista[c][v] %2 == 0:
            partot += lista[c][v]

maximo = max(lista[1])
print()
print(f'A soma de todos os valores pares é {partot}')
print(f'A da terceira coluna é {tot3}')
print(f'O maior valor da segunda linha é {maximo}')
