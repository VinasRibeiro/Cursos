'''

Crie um programa que vai ler vários números e colcoar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,
respectivamente.

Ao final, mostre o conteúdo das três listas gerados.

'''

lista = list()
impar = list()
par = list()
pos = 0

while True:

    lista.append(int(input('Insira um numero')))

    if lista[pos] % 2 == 0 :
        par.append(lista[pos])
    else:
        impar.append(lista[pos])
    pos+=1

    escolha = str(input('deseja continuar?')).strip().upper()[0]

    if escolha == 'N':
        break


print(len(lista))



print(f'Numeros impares {impar}')
print(f'Numeros pares {par}')
print(f'Total: {lista}')


