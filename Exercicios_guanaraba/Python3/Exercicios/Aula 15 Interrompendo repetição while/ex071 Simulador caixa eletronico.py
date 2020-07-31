'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar
qualtas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

primeira versão

vuser = int(input('Valor de saque: '))
c50 = c20 = c10 = c1 = 0

while vuser >= 50:
    vuser -=50
    c50 += 1
while vuser >= 20:
    vuser -=20
    c20 += 1
while vuser >= 10:
    vuser -=10
    c10 += 1
while vuser >= 1:
    vuser -= 1
    c1 += 1

print(f'50:{c50}\n20:{c20}\n10:{c10}\n1:{c1}')

'''

valor = int(input('Qual o valor a sacar? R$: '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -=céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0

        if total == 0:
            break






# Código do professor


