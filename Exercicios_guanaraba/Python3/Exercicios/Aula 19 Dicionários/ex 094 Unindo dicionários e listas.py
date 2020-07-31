'''

Crie um programa que leia nome,sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.

'''



pessoas = list()
dados = dict()
mulheres = list()
acimedia = list()
escolha = ''
media = 0
total = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    total = total + dados['idade']

    while True:

        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Digito errado')

    if dados['sexo'] == 'F':
        mulheres.append(dados.copy())
    pessoas.append(dados.copy())

    while True:

        escolha = str(input('Gostaria de continuar? [S/N]: ')).upper()[0]
        if escolha in 'SN':
            break
        print('Digito errado')

    if escolha in 'N':
        break
print(len(pessoas))
media = total / len(pessoas)

for c in range(0,len(pessoas)):
    if pessoas[c]['idade'] >= media:
        acimedia.append(pessoas[c])



print(f'Foram cadastrados {len(pessoas)} pessoas')
print(f'A média é {media}')
print(f'As mulheres do grupo são ', end='')

for c in mulheres:
    print(f'{c["nome"] }', end='')

print()

print(f'As pessoas acima da média são', end='')
for c in acimedia:
    print(f'{c["nome"]} ', end='')
print()






