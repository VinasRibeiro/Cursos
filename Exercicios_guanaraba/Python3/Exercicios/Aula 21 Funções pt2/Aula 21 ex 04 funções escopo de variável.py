'''
def teste():
    x = 0
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')



# Programa Principal
n=2
print(f'Na função teste, n vale {n}')
print(f'Na função teste, x vale {x}')
esse código daria errado pois a variável x só funciona dentro da função
'''

def funcao():
    #Este n1 esta dentro e vale 4 é local.
    n1 =4
    print(f'N1 dentro vale {n1}')

#Este n1 esta fora e vale 2 é global
n1 = 2
print(f'N1 fora vale {n1}')