'''
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor
digitado for impar. desconsidere-o.

minha versão
numero = [1,1,1,1,1,1]
result = 0

for c in range(0,6):
    numero[c] = (int(input('Insira o numero {}: '.format(c+1))))

for c in range (0,6):
    if numero[c] % 2 == 0:
        result += numero[c]
'''

#versão do professor
soma=0
cont=0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Voce informou {} números pares e a soma foi {}'.format(cont, soma))



print(result)

