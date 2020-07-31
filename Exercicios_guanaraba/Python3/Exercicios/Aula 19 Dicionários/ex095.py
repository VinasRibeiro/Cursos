'''

Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.

'''

jogadores = list()
dados = dict()
gols = list()
teste = 0

while True:

    dados.clear()
    gols.clear()

    dados['jogador'] = str(input('Nome do jogador: '))
    dados['Partidas'] = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

    for c in range(0,dados['Partidas']):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))


    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())


    escolha = str(input('Gostaria de continuar?: [S/N]')).upper()[0]
    if escolha == 'N':
        break


'''
Mostrar cabeçalho com for
Neste caso, o for pega as chaves que estão em dados que são respectivamente, 'jogadores', 'Partidas', 'Gols' e 'Total'
pq quando o if escolha foi executado ele saiu do loop e ficou essas informações dentro de 'dados' então é possível
usar essas informações nas chaves de dados para fazer um cabeçalho, como no código abaixo.
for recebe as chaves de dados e exibe com um espaçamento de 15 caracteres cada.
'''
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)


'''
O enumerate aqui esta colocando no 'k' as posição ou chave da lista e no v o valor correspondente 
Ou seja o for sempre começa com 0 que é a posição inicial de qualquer lista
OBS: toda lista sempre começa com 0
Para mostrar só os valores do dicionário que esta em cada posição da lista precisa de outro loop for
com a função values() que coloca na variável d só o conteudo do dicionário inteiro dentro da posição k de jogadores
'''
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

#Código para busca de jogadores
while True:
    busca = int(input('Mostrar qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do jogador {jogadores[busca]["jogador"]}:')
        for i, g in enumerate(jogadores[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)


