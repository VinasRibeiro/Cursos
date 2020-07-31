'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
-Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÂO
-Média 7.0 ou superior:
APROVADO

'''

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

média = (nota1 + nota2) / 2

if média < 5.0:
    print('Reprovado')
elif média <= 6.9:
    print('Recuperação')
elif média > 6.9:
    print('Aprovado')

