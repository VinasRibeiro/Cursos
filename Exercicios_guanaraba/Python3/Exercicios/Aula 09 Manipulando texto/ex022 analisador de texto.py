'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1 O nome com todas as letras maiúsculas

2 O nome com todas minúsculas

3 Quantas letras ao todo sem considerar espaços

4 Quantas letras tem o primeiro nome

'''


#primeira forma de fazer
'''
nome=str(input("Insira seu nome completo: ")).strip()
nomediv = nome.split()
print('Nome em maiusculo {} '
      '\nNome em minusculo {} '
      '\nQuantidade de letras {}'
      '\nO primeiro nome tem {} Letras '
      .format(nome.upper(),nome.lower(),len(nome)-nome.count(' '),len(nomediv[0])))
'''

#Segunda forma de fazer

nome=str(input("Insira seu nome completo: ")).strip()
print('Nome em maiusculo {} '
      '\nNome em minusculo {} '
      '\nQuantidade de letras {}'
      '\nO primeiro nome tem {} Letras '
      .format(nome.upper(),nome.lower(),len(nome)-nome.count(' '),nome.find(' ')))
'''
Com a função find retorna a posição do primeiro espaço o que pela regra da numeração de 0 a ...
a posição será o numero que a primeira palavra contém no caso posição 3 que é igual o tamanho do primeiro nome
'''