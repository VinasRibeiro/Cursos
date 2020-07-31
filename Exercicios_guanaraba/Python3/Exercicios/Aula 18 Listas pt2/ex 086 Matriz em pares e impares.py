'''

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.


Ex:
 _ _ _
|_|_|_|
|_|_|_|
|_|_|_|




No final, mostra a matriz na tela, com a formatação correta.

'''

lista = [[],[],[]]
n = 0

for c in range(0,3):
    for v in range(0,3):
        n = int(input(f'Digite o numero para [{c},{v}]'))
        lista[c].append(n)

for c in range(0,3):
    print()
    for v in range(0,3):
        print(f'[{lista[c][v]:^5}]', end='')




