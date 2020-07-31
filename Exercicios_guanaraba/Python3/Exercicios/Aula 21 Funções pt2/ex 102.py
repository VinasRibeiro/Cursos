'''

Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.

'''


def fatorial(n, show = False):
    """
    -->Calcula o fatorial de um numero.
    :param n: È o numero a ser fatorado
    :param show: é a condição mostra ou não como foi feito o calculo fatorial
    :return: O valor fatorial de um numero n.
    """

    fator=1
    while n > 0:

        if show:
            print(f'{n} ',end='')
            print('x ' if n > 1 else' = ',end='')
        fator=fator*n

        n-=1

    print(fator)




n = int(input('Insira o numero: '))


fatorial(n)
