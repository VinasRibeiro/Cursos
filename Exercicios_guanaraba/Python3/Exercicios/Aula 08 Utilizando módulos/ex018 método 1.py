#Faça um programa que leia um angulo qualquer e mostra na tela o valor do seno cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que você deseja: '))
#È nescessario converter primeiro de graus para radianos
seno = sin(radians(ângulo))
#radians() converte o numero para radianos e sin() calcula o seno
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))



