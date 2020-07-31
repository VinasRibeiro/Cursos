'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

Se o ano NÃO é divisível por 4, então, ele não é bissexto.
Exemplo: 2018

Se é um ano que é divisível por 4 e por 100, mas não é divisível por 400, então ele NÃO é um ano bissexto.
Exemplo: 2100

Se o ano em questão é divisível por 4, verifique se é
divisível por 100 também, se for, verifique se o número é divisível por 400, se
sim, o ano é bissexto.
Exemplo: 2000

Se o ano é divisível por 4 e NÃO é divisível por 100, então,
trata-se de um bissexto.
Exemplo: 2016.

minha solução

ano = int(input('Insira o ano: '))
frasesim = 'O ano é Bissexto'
frasenao = 'O ano não é Bissexto'

print('Divisão por 4   :{}'.format(ano%4))
print('Divisão por 100 :{}'.format(ano%100))
print('Divisão por 400 :{}'.format(ano%400))


if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('O ano de {} é Bissexto '.format(ano))
        else:
            print('O ano de {} não é Bissexto '.format(ano))
    else:
        print('O ano de {} é Bissexto '.format(ano))
else:
    print('O ano {} não é Bissexto '.format(ano))
'''

#Solução do curso em video

from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO'.format(ano))