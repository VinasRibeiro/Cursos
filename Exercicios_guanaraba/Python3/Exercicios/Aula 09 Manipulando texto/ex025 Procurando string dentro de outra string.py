'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
'''
nome=str(input('Insira seu nome :')).strip()
'''
com essa atribuição de transformar toda a frase em minusculo 
ajuda a reconhecer qualquer palavra silva mesmo ela contendo letras maiusculas ou minusculas
'''
nomelower = nome.lower()
print('A pesquisa sobre silva em {} retornou :{}'.format(nome, 'silva' in nomelower))

