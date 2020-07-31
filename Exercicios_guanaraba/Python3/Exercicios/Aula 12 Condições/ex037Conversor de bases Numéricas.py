'''
Escreva um programa que leia um número inteiro qualquer e
peça para o usurário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 hexadecimal
'''

n1 = int(input('Insira um numero: '))

convert = int(input("Qual base você gostaria de converter? \n1 para binário "
                    "\n2 para octal"
                    "\n3 para hexadecimal\n>"))
if convert > 3:
    print('Esta opção não esta desponivel')
elif convert == 3:
    print('O hexadecimal de {} é {}'.format(n1,hex(n1)[2:]))
elif convert == 2:
    print('O octal de {} é {}'.format(n1,oct(n1)[2:]))
elif convert == 1:
    print('O binário de {} é {}'.format(n1,bin(n1)[2:]))
