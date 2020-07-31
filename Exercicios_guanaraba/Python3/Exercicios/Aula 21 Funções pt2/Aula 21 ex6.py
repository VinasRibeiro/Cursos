def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
#Neste caso a função retorna verdadeiro ou falso
#Como todas as repetições das linguagem trabalham com isso.
#O if altomaticamente verifica se é True ou False e executa a sua ação normalmente.

if par(num):
    print('PAR')
else:
    print('IMPAR')