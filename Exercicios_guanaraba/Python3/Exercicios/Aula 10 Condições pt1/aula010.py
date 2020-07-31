'''forma simples
nome = str(input('Insira um nome: '))
if nome == 'Gustavo':
    print('Ola {} seu nome é tão lindo'.format(nome))
print('Bom dia {}'.format(nome))
'''

#forma composta
'''
nome = str(input('Insira um nome: '))
if nome == 'Gustavo':
    print('Ola {} seu nome é tão lindo: '.format(nome))
else:
    print('O seu nome é bem normal')

print('Bom dia {}'.format(nome))
'''


#forma em uma linha só
nome = 'vini'
print('Parabéns'if nome == 'vini' else 'Nome incorreto')
#note que a condição positiva é o primeiro bloco e a negativa vem depois da condição digitada