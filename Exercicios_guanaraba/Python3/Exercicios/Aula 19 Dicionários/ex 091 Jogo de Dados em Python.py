'''

Crie um programa aonde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

'''

#versão do professor

from random import randint
from operator import itemgetter

jogo = {'Jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = dict()

print('Valores sorteados:')

'''
quando vc tem um dicionário, ele não tem masi as posições numericas,
para conseguir isso tem que usar o metodo items() no dicionário, ele numera as referencias jogadores
mas não altera o dicionário só numera para ser usado em um for por exemplo.

'''

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

'''
o dicionário ranking para poder usar a função sorted tem que usar desta forma
o python acaba convertendo para lista e colocando na variavél ranking
o itemgetter faz com que vc escolha em qual dos vetores vc quer organizar
No exemplo abaixo ele organiza pelo valor 1 que é o numero gerado randomicamente
ele poderia organizar por jogadores mas não é o proposito do programa, e o reverse=True
faz com que ele coloque em ordem decrecente.

'''

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')



