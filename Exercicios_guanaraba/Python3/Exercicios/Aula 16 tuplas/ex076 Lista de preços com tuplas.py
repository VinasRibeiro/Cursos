'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.


material = ('Lapis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila',120.32,
            'Caneta', 22.30)

for c in range(0,len(material)):

    if c % 2 != 0:
        print(f'{material[c]:>}',end='')

    if c % 2 ==0:
        print(f'{material[c]}', end='')
        print('.'*(20-len(material[c])),end='R$  ')
    else:
        print('')

print('FIM')
'''
#código do professor

material = ('Lapis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila',120.32,
            'Caneta', 22.30)

print(f'{"Lista de materiais":^40}')
#pos significa posição
for pos in range(0,len(material)):
    if pos %2 == 0:
# o simbolo de : significa uma tabulação ou seja, o espaço de 30 caracteres
# com a palavra e o restante com os pontos até chegar a 30 caracteres de alocação.
        print(f'{material[pos]:.<30}', end='')
    else:
#o mesmo se aplica aqui porém sem pontos e alinhado a direita com alocação de 7 caracteres e com duas casa depois da virgula.
        print(f'R${material[pos]:>7.2f}')
