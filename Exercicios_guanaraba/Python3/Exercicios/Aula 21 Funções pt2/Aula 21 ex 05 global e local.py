def teste(b):
    #Neste caso a variável 'a' vai vir de fora do programa pra dentro
    #A variavel 'a' aqui vai receber 5 e depois 8 e a variável global vai ter o valor 8 tbm
    #Ou seja a variavel com o comando global faz com que a função não retorne numero nenhum
    #Mas ela conseguil alterar uma variável de fora com o comando global.
    
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')