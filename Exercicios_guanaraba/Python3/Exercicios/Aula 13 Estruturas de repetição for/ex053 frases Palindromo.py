'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconcideramdo os espaços.

Ex.
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''

#Código do professor
# a função upper converte tudo para maiusculo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#O mesmo resultado do for é possivél com o seguinte código.
#inverso = junto[::-1]


#Para resolver, é nescessário separar as palavras da frase com split() depois juntalas com join()
#Assim toda a frase vai ficar sem espaços no meio.

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palimdromo!)
else:
    print('A frase não é um palimdromo!')


