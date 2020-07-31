'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = float(input('N1:'))
n2 = float(input('N2:'))
n3 = float(input('N3:'))

n = [n1,n2,n3]
if n1 > n2 and n1 > n3:
    n[0] = n1
    if n2 > n3:
        n[1] = n2
        n[2] = n3
    else:
        n[1] = n3
        n[2] = n2
elif n2 > n1 and n2 > n3:
    n[0] = n2
    if n1 > n3:
        n[1] = n1
        n[2] = n3
    else:
        n[1] = n3
        n[2] = n1
elif n3 > n1 and n3 > n2:
    n[0] = n3
    if n2 > n1:
        n[1] = n2
        n[2] = n1
    else:
        n[1] = n1
        n[2] = n2
else:
    print('deu ruim')

print('{} é maior que {} que é maior que {}'.format(n[0],n[1],n[2]))

'''

a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))

#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor numer é {}'.format(menor))
print('O maior numero é {}'.format(maior))






