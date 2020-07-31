'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solcitada em cada caso.



c=0
sair=5
escolha = 4

while sair == 5:

    if escolha == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))

    elif escolha == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif escolha == 3:

        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n1 == n2:
            print('{} é igual a {}'.format(n1,n2))
        else:
            print('{} é maior que {}'.format(n2,n1))
    elif escolha == 4:
        if c != 0:
            print('Insira novamente os numeros')
        n1 = int(input('Insira 1º valor: '))
        n2 = int(input('Insira 2º valor: '))
    elif escolha == 5:
        sair = 4
    else:
        print('Esta escolha não existe')
    if sair == 5:
        escolha = int(input('[1] somar \n[2] Multiplicar \n[3]Maior \n[4]novos numeros \n[5]sair do programa \n>'))
        c+=1
'''

#Código do professor


n1 = int(input('Insira 1º valor: '))
n2 = int(input('Insira 2º valor: '))
escolha = 0

while escolha != 5:

    escolha = int(input('[1] somar \n[2] Multiplicar \n[3]Maior \n[4]novos numeros \n[5]sair do programa \n>'))

    if escolha == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))

    elif escolha == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif escolha == 3:

        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n1 == n2:
            print('{} é igual a {}'.format(n1,n2))
        else:
            print('{} é maior que {}'.format(n2,n1))
    elif escolha == 4:

        print('Insira novamente os numeros')
        n1 = int(input('Insira 1º valor: '))
        n2 = int(input('Insira 2º valor: '))
    elif escolha == 5:
        print('Até mais')
    else:
        print('Esta escolha não existe')








