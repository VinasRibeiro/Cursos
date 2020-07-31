'''
Faça um programa que leia um numero inteiro e diga
se ele é ou não um numero primo.
'''


#Código do professor

num = int(input('Insira um numero: '))

tot = 0

for c in range(1,num + 1):
    if num % c ==0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele Não é primo!')
