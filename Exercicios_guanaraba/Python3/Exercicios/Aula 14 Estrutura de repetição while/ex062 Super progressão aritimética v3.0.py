'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar masi alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.

termo = 1
c=1
while termo != 0:
    c = 1
    termo=int(input('Primeiro termo da PA: '))
    if termo != 0:
        razão=int(input('Insira a razão da PA: '))
        print(termo,end='')
        while c < 10:
            termo = termo + razão
            print('-{}'.format(termo),end='')
            c+=1
        print('')
print('FIM')
'''

#Código do professor

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos vc quer ver mais? '))
print('Progressão aritmética')
