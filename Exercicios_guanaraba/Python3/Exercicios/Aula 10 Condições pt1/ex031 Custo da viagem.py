'''
Desenvolva um programa que pergunte a distância de uma viagem em km,
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

minha solução
dist = float(input('Insira a distancia: '))

if dist >= 200:
    print('Você ganhou um desconto pois a distancia esta acima de 200KM \nO total a pagar é R${} '.format(dist*0.45))
else:
    print('O total a pagar é R${} '.format(dist*0.50))
'''

#Solução do curso em video

distância = float(input('QUal é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))