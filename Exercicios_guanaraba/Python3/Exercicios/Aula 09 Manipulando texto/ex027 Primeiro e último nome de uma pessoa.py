'''
Faça um programa que leia o nome completo de uma pessoam, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
Último = Souza
'''
nome=(str(input('Insira um nome :'))).strip()
nomediv = nome.split()
print('O primeiro nome é: {} \nO Último nome é: {}'.format(nomediv[0],nomediv[len(nomediv)-1]))

