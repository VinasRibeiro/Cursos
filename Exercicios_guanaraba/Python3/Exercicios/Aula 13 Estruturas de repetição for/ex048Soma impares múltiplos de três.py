'''
Faça um programa que calcule a soma entre todos os números impares que
são multiplos de 3 e que se encontram no  intervalo entre 1 até 500.
'''
'''
num = 0

for c in range(1,501):
    if c%2 !=0:
        if c%3 == 0:
            num = num + c


print('A soma dos numeros de 1 a 500 e multiplos de 3 é {}'.format(num))
'''
#Código do professor

soma = 0
#O numero 2 no final disponibiliza os numeros impares na repetição.
for c in range(1,501,2):
    if c % 3 ==0:
        soma += c
print('A soma de todos os valores solicitados é {}'.format(soma))