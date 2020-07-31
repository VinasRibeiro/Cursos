'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A)Qual é o total gasto na compra.
B)Quantos produtos custam mais de R$1000.
C)Qual é o nome do produto mais barato.
'''
total = 0
menor = 0
c=0
cmaior = 0

while True:
    produto = str(input('Produto: ')).strip()
    preço = float(input('Preço: '))

    if c == 0 or preço < menor:
        menor = preço
        produtomenor = produto


    if preço > 1000:
        cmaior += 1

    c += 1
    total += preço
    resposta = str(input('Gostaria de continuar?')).strip().upper()[0]
    if resposta == 'N':
        break


print(f'Total da compra é R${total}, \n{cmaior} custam mais que R$1000')
print(f'O produto mais barato foi {produtomenor} que custa R${menor}')