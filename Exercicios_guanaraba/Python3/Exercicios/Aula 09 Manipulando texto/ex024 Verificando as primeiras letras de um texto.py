'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
'''

''' primeira forma com atrubuição in e duas variáveis
nome=str(input('Insira o nome da cidade: ')).strip()
nomediv=nome.split()

print('A cidade começa com Santo? :{}'.format('santo' in nomediv[0].lower()))
'''

# Segunda forma com uma variável
cid = str(input('Insira a cidade: ')).strip()
print('A cidade começa com santo? : ',cid[:5].upper() == 'SANTO')
print('\n',cid[:5])


