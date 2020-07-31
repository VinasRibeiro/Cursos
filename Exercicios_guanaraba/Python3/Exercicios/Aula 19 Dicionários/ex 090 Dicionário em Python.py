'''

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.

'''



aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = int(input('Insira a média: '))

print(f'Nome é {aluno["nome"]} e a média é: {aluno["media"]}')
print(aluno)


