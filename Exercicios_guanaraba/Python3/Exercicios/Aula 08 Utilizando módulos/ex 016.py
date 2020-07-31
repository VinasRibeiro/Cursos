#crie um programa que leia um número Real qualquer e mostre na tela a sua porção inteira
#ex:
#Digite um numero: 6.127 A porção inteira retorna 6.


#1 primeira maneira
'''from math import trunc
num = float(input("Insira um numero quebrado :"))
result= trunc(num)
#módulo trunc() é usada para remover os numeros depois da virgula
print(' o resultado inteiro é : {}'.format(result))
print('Esta função trunc() retorna o valor sem os numeros depois da virgula')'''

num = float(input('Digite um numero: '))
#O metodo int() retorna o mesmo resultado que o trunc() porém é um método que ja vem com o python
#O método trunc() pertence a biblioteca math
print('O numero digitado é {} e sua porção inteira é {}'.format(num, int(num)))


