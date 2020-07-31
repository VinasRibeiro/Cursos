'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-Até 9anos: MIRIM
-Até 14anos:INFANTIL
-Até 19 anos:Junior
-Até 20 : Sênior
acima: Master


'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento'))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é infantil')
elif idade <= 19:
    print('Sua categoria é junior')
elif idade <= 20:
    print('Sua categoria é Sênior')
elif idade > 20:
    print('Sua categoria é Master')