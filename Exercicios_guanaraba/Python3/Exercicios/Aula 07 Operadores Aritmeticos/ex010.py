#ex010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#cotação considerada US$ 1,00 = R$ 3,27


mony=float(input('Quantos reais você tem? '))
doll=float(input('Insira a cotação do dolar: '))
result=mony*doll
print('Você tem {:.2f} reais em dolares'.format(result))