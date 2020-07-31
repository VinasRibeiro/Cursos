#ex008
#Escreva um programa que leia um valor em metros e p exbia convertido em centimetros e milimetros.


mts = float(input('Insira a metragem: '))
cent = mts * 100
mli = mts * 1000
print(' A medida em centimetros é: {} \n A medida em milimetros é {}'.format(cent, mli))
