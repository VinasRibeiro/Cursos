'''
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".

Em que posição ela aparece a primeira vez.

Em que posição ela aparece a última vez.
'''
palavra = str(input('Insira uma palavra :')).strip()
letra = str(input('Insira uma letra :'))
print("""A letra {} esta na palavra {}, {} vezes 
\nEla aparece a primeira vez na casa {} 
\nNa ultima vez na casa {}"""
      .format(letra,palavra,palavra.lower().count(letra.lower()),palavra.lower().find(letra.lower())+1,palavra.lower().rfind(letra.lower())+1))


