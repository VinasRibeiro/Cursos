#Utilizando modulos
#Metodos são um conjunto de funções ex

#math é uma biblioteca que junta varios modulos

#ex
#ceil= Arredonda um numero float para cima
#Floor = Arredonda um numero float para baixo
#Trunc = Trunca o numero, elimina o numero da virgula para frente
#Pow = Potênciação
#sqrt = calcula a raiz quadrada
#factorial = calcula a fatorial do numero

#para usar o metodo use a sintax

#import e from = comandos para chamar a biblioteca

#ex
#import math

#importa todos os módulos da biblioteca math, não aconcelhado no caso de usar poucos módulos, isso ocupa um espaço
#na memoria desnecessário.

#from math import sqrt
#assim ele importa somnete o módulo sqrt da biblioteca math

#from math import sqrt, ceil
#com a virgula vc importa mais de um módulo para

#isso importa a biblioteca math
#import math
#num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
#quando se importa a biblioteca interira é nescessário especificar depois qual o módulo usado
#como no caso acima
#print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

from math import sqrt
num = int(input('Digite um numero'))
raiz = sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num,raiz))









