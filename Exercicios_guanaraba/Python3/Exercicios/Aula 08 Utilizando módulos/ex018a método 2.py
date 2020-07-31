from math import radians, sin, cos, tan

ângulo = float(input('Digite o angulo: '))
radiano = radians(ângulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print('O ãngulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
print('O Angulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))
