'''

Crie um programa que vai ler vários números
e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenados de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

'''
lista = list()
c = n = 0

while True:

    n = int(input('Insira um numero: '))
    lista.append(n)
    c+=1
    escolha = str(input('Deseja continuar:')).strip().upper()[0]

    if escolha in 'N':
        break


lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {c} valores')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')