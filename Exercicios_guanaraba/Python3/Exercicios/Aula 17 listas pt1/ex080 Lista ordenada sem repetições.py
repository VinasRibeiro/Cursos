'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.



n = list()
n2 = 0
for c in range(0,5):
    n2 = int(input('Insira um numero: '))


    if len(n) == 0:
        n.insert(0, n2)
        print('vazio')
    else:
        for b in range(0,len(n)):

            if n[b] < min(n):
                n.insert(b,n2)
'''
#Código do professor

lisra = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1












print(n)




