'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final,
mostre quantos números foram digitados e qual foi a a soma entre eles
(desconciderando o flag).
'''

cont = soma =0
while True:
    n1 = int(input('insira um numero: '))
    if n1 == 999:
        break
    else:
        cont += 1
        soma += n1

print(f'Numero de vezes {cont}, a soam dos numeros é{soma}')
print('FIM')

