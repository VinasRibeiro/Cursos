#ex015
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantodade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, Sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

d=float(input('Quantos dias o carro foi alugado :'))
km=float(input('Quantos kilometros foram usados :'))

result=(d*60)+(km*0.15)

print('O valor total é {:.2f}'.format(result))
