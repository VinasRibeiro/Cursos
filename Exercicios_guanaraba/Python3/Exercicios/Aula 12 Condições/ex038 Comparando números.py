'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
-O primeiro valor é
maior
-O segundo valor é
menor
-Não existe valor maior, os dois são
iguais
'''

Na = int(input('Insira o numero a: '))
Nb = int(input('Insira o numero b: '))

if Na == Nb:
    print('Os numeros {} e {} são iguais'.format(Na,Nb))
elif Na > Nb:
    print('Os numeros {} é maior que {}'.format(Na,Nb))
elif Na < Nb:
    print('Os numeros {} é menor que {}'.format(Na,Nb))

'''
Código feito pelo professor

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo numero é maior')
else:
    print('Os dois valores são iguais')
'''


