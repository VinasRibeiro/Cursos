'''

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro
e mostre uma mensagem com tamanho adaptável.

EX:
escreva('Ola, Mundo!')

saida:
------------
Olá, Mundo!
------------

'''

def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)



texto = str(input('Coloque o texto: '))
escreva(texto)



