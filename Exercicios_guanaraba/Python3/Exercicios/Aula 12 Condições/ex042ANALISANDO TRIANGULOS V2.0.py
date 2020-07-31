'''
Refaça o DESAFIO 035 dos trinãngulos, acrecentando o recurso de mostrar que tipo de triãngulo será formado:
-Esquilátero:todos os lados iguais.
-Isóceles:dois lados iguais
-Escaleno:todos os lados diferentes


minha versão
r1 = float(input('Insira a reta 1: '))
r2 = float(input('Insira a reta 2: '))
r3 = float(input('Insira a reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('O triangulo existe')

    if r1 == r2 and r1 == r3:
        print('Este é um triangulo equilátero.')

    if r1 == r2 and r1 != r3:
        print('Este é um triangulo Isóceles.')
    elif r2 == r3 and r2 !=r1:
        print('Este é um triangulo Isóceles.')
    elif r3 == r1 and r3 != r2:
        print('Este é um triangulo Isóceles.')

    if r1 != r2 and r1 != r3 and r2 != r3:
        print('Este é um triangulo escaleno')

else:
    print('O triangulo não é possível')
'''

#versão do professor

r1 = float(input('Insira a reta 1: '))
r2 = float(input('Insira a reta 2: '))
r3 = float(input('Insira a reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('O triangulo existe')

    if r1 == r2 == r3:
        print('EQUILATERO! ')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO! ')
    else:
        print('ISOCELES')

else:
    print('O triangulo não é possível')