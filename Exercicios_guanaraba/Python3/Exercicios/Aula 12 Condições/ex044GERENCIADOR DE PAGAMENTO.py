'''
Elabore um programa que calcule o valor a se pago por um produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque:10% de desconto
-À vista no cartão:5% de desconto
-EM até 2x no cartão: preço normal
-3X ou mais no cartão: 20% de juros

'''
produto = float(input('Insira o valor do produto :'))

escolha = int(input('Escolha a opção \nÀ vista: 1 \nParcelado: 2 \n'))

if escolha == 1:
    escolha = int(input('Á vista Dinheiro/Cheque: 1 ou Cartão: 2\n'))
    if escolha == 1:
        produto = produto - ((produto/100)*10)
        print('O valor final é de {} reais, com 10% de desconto'.format(produto))
    elif escolha == 2:
        produto = produto - ((produto/100)*5)
        print('O valor final é de {} reais, com 5% de desconto'.format(produto))
    elif escolha >2:
        print('Você escolheu uma opção que não existe')
else:
    escolha = int(input('Quantas parcelas?:'))
    if escolha <= 2:
        print('Pagamento em 2x o preço final é {}.'.format(produto))
    else:
        produto = produto + (produto/100*20)
        print('Você escolheu mais que 2 o preço total é {}'.format(produto))