'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


metodo não confirmado

frase = str('))Teste((')
pdir = 0
pesq = 0
pdvezes = frase.count('(')
pevezes = frase.count(')')

if pdir == pesq:
    print('Os parenteses estão corretos')

    pdir = frase.index('(')
    print(pdir)

    pesq = frase.index(')')
    print(pesq)

    if pdir <= pesq:
        print('O primeiro parenteses esta correto')
    else:
        print('O primeiro parenteses esta incorreto')


else:
    print('Os parenteses não estão fechados corretamente')
print(f'( Existe {pdvezes}')
print(f') Existe {pevezes}')

outro metodo

frase = str(input('Coloque uma espressão')).strip()

pdvezes = frase.count('(')
pevezes = frase.count(')')

if pdvezes == pevezes:
    print('Sua expressão esta correta')
else:
    print('Sua espressão esta errada')

print(f'( Existe {pdvezes}')
print(f') Existe {pevezes}')
'''

#Código do professor

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')




