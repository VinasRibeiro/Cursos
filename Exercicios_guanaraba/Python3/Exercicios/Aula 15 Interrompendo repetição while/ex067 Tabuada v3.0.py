'''
Faça um programa que mostre a tabuada de vários numeros, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''




while True:
    n1 = int(input('Numero da tabuada: '))
    if n1 < 0:
        break

    c = 1
    while c <= 10:
        print(f'{c} x {n1} = {c*n1}')
        c+=1
print('FIM')

'''
Código do professor

È o quase o mesmo código porém usando o for para gerar a tabuada
assim não tem a necessidade de atribuir uma variavel c = 1, como descrito acima.
