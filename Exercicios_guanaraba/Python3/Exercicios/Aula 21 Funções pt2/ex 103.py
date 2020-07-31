'''

Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de
um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.



def ficha(a, b=0):


    if a == '':
        print('Nome não informado')
    else:
        print(f'O nome é {a}')
    if b == 0:
        print('Gols não informado')
    else:
        print(f'Ele fez {b} gols')




nome = str(input('Nome jogador: '))
gols = int(input('Gols: '))

ficha(nome, gols)


'''

#Código do professor

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

#Programa principal

n = str(input("Nome do jogador: "))
g = str(input("Numero de Gols: "))

#A função .isnumeric() verifica se uma string contém só numeros
#Se tiver letras no meio ela considera q não é numero.

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = 0)
else:
    ficha(n, g)

