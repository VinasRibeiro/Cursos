'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) OS últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.

'''

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atético-PR', 'Bahia', 'São paulo', 'Fluminense','Sport Recife', 'EC Vitória', 'Coritiba',
         'Avai', 'Ponte preta', 'Atlético-GO')

print(f'A lista dos times é {times}')
print(f'Os cinco primeiros são: {times[0:5]}')
print(f'Os 4 ultimos são: {times[16:]}')
#pode ser usado desta forma tbm
print(f'Os 4 ultimos são :{times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posição')





