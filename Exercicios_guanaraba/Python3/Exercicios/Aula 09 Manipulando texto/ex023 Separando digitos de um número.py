'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

Ex
Digite um número:1834

unidade:4
dezena:3
centena:8
milhar:1

'''
#primeira forma
'''
numero = str(input('Insira um numero :'))

print('Unidade :{} \nDezena :{} \nCentena :{} \nMilhar {}'.format(numero[3],numero[2],numero[1],numero[0]))
'''

#segunda forma maneira matemática

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O numero {} é:'.format(num))
print('Unidade {} \nDezena {} \nCentena {} \nMilhar {}'.format(u,d,c,m))

'''obs da forma matemática qualque numero que você coloque será reconhecido pelo programa, 
inclusive se o numero digitado for maior que o que o programa reconhece, porém mostrando somente os 4 primeiros digitos
'''


