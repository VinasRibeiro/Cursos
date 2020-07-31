'''

Crie um programa que tenha a função leiaint(), que vai funcionar de forma
semelhante á função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.

EX:
n = leiaint('Digite um n')

'''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;33mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero')
print(f'Você digitou o numero {n}')