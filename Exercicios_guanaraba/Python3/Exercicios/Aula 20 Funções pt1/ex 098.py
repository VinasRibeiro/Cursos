'''

Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo
e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a)De 1 até 10, de 1 em 1
b)De 10 até 0, de 2 em 2
c)Uma contagem personalisada


'''
from time import sleep
#A função sleep na versão atual para funcionar é preciso solocar flush=True em todo print
#Para aparecer um print de cada vez, em outro


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {1} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')




#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)


