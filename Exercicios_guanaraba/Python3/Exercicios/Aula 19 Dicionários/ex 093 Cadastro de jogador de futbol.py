'''

Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

'''


dados = dict()
gols = list()
total = 0
dados['jogador'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

for c in range(0,dados['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    total += gols[c]

dados['Gols'] = gols[:]
dados['Total'] = total



#enumerate é um metodo usado em lista,
#Ou seja, para usar no for uma lista que esta dentro de um dicionário, precisa usar enumerate
#O enumerate pega a lista dentro do dicionário gols e coloca na variavel "i" e "v" respectivamente
#Assim o for consegue mostrar todo o conteudo da lista dentro de gols

for i, v in enumerate(dados["Gols"]):
    print(f'Na partida {i}, fez {v} gols')

print(dados)