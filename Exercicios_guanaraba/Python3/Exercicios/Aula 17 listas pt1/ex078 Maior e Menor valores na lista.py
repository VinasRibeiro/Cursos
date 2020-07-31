'''
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

'''
valores=[]

for c in range(0,5):
    valores.append(int(input(f'Valor {c+1}')))


print(f'O maior numero foi {max(valores)} na posição ',end='')
for c in range(0,5):
    if valores[c] == max(valores):
        print(f'{c}.. ',end='')

print(f'\nO menor numero foi {min(valores)} na posição ',end='')
for c in range(0,5):
    if valores[c] == min(valores):
        print(f'{c}.. ',end='')

#Código do professor, sem usar função min e max, que faria com que o programa usa-se mais processamento


listanum = []
mai = 0
men = 0

for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Voçê digitou os valores {listanum}')
print(f'O maior valor Digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ',end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()


