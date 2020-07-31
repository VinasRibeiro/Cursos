'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.


primeiro exemplo

pessoas = list()
lista = list()
maior = list()
menor = list()
media = 0
pesotot = 0
cont=0
while True:

    pessoas.append(str(input('Nome')))
    pessoas.append(float(input('Peso')))
    lista.append(pessoas[:])
    pessoas.clear()
    pesotot = pesotot + lista[cont][1]
    cont+=1

    escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break

media = pesotot / len(lista)

for c in range(0,len(lista)):

    if lista[c][1] > media:
        maior.append(lista[c][0])
        maior.append(lista[c][1])

    if lista[c][1] < media:
        menor.append(lista[c][0])
        menor.append(lista[c][1])


print(f'O total de pessoas foi {cont}')



print(pesotot)
print(media)
print(len(lista))
print(lista)
print(maior)
print(menor)
print(maior[-1])
print(lista.sort())
'''

#Versão do professor

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? :'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas. ')

print(f'O maior peso foi de {mai}Kg Peso de ',end='')

for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men}Kg.Peso de ', end='')

for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
print()

print(princ)
