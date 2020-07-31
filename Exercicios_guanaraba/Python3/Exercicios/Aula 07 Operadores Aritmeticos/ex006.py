#ex006
#Crie um algoritimo que leia um número e mostre o seu dobro triplo e raiz quadrada.

n1=int(input('insira n1: '))
n2=n1*2
n3=n1*3
n4=(n1**(1/2))

print(' O dobro de n1 é: {} \n O triplo de n1 é: {} \n A raiz quadrada de n1 é : {:.2f}'.format(n2,n3,n4))