'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter im valor correto.



c = 0

while c == 0:
    sexo = str(input('Insira o seu sexo [M ou F]: ')).upper()

    if sexo == 'M':
        print('Você é HOMEM')
        c = 1
    elif sexo =='F':
        print('Você é MULHER')
        c = 1
    elif sexo != 'F' or sexo != 'M':
        print('Vc digitou errado por favor ', end='')


print('Fim')

'''


#Código do professor

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Por Favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))