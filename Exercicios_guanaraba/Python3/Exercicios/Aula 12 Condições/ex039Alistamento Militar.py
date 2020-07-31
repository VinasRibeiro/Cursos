'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
e acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
'''
''' Minha versão saiu errada
from datetime import date
anoidade = int(input('Insira o ano em que vc nasceu: '))
ano = date.today()
result = ano.year - anoidade
if result == 18:
    print('Você tem {} e esta no perido de alistamento'.format(result))
elif result < 18:
    falta = 18 - result
    print('Você tem {} anos e falta {} anos para o alistamento'.format(result,falta))
elif result > 18:
    passou = result -18
    print('Você tem {} anos e ja passou {} anos do seu alistamento'.format(result,passou))
'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))

