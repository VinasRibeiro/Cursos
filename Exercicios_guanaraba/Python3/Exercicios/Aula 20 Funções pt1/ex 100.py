'''

Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

'''

from random import randint



def sorteio(randlista,qnum):

    for c in range(0, qnum):
        randlista.append(randint(1, 10))



def somaPar(randlista):
    resultado = 0
    for c in range(0,len(randlista)):
        if randlista[c] % 2==0:
            resultado = resultado + randlista[c]

    return resultado





lista1 = list()

qnum = int(input('Quantos numeros sortear? '))

#Todas variáveis de fora de uma função ou classe são globais

sorteio(lista1,qnum)
print(f'Os numeros são ',lista1)

somaPar(lista1)
print(f'A soma é {somaPar(lista1)}')

