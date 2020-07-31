'''

Faça um programa que tenha uma função chamada maior(), que receba vários parámetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''

def maior(valorl):
    maior = 0

    for c, v in enumerate(valorl):
        if valorl[c] > maior:
            maior = valorl[c]

    return maior



lista = []

while True:
    lista.append(int(input('Insira um valor: ')))
    escolha = str(input('Gostaria de continuar? '))
    if escolha in 'Nn':
        break


print(maior(lista))


