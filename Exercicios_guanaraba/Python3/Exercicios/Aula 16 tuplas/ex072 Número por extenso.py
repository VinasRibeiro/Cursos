'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.
'''
palavra = ('UM','DOIS','TRÊS','QUATRO','CINCO','SEIS')


while True:
    user=int(input('Digite o numer de 1 a 6 '))
    #Metodo do professor, duas comparações com uma variável a variavél user tem que estar entre 1 e 6
    if 1 <= user <= 6:
        break
    print('vc digitou errado. ')

print(f'Você digitou o numero {palavra[user-1]}')
