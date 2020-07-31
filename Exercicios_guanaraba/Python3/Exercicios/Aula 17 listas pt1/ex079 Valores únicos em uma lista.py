'''
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista.Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

listanum=list()
num = 0
print('Primeira parte')

while True:
    num = int(input('Insira um valor'))

    if num in listanum:
        print('Esse valor ja existe')
    else:
        listanum.append(num)


    opção = str(input('Deseja continuar?')).strip().upper()[0]
    while opção not in 'SsNn':
        opção = str(input('Opção errada, digite novamente')).strip().upper()[0]

    if opção == 'N':
        break



listanum.sort()
print(f"Os numeros foram {listanum}")
