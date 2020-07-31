'''

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário.

Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.



from datetime import date


trabalhador = dict()

atual = date.today().year

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho: '))
trabalhador['idade'] = atual - trabalhador['nascimento']

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = int(input('Salário: '))

print(f'O nome é {trabalhador["nome"]}')
print(f'A idade é {trabalhador["idade"]}')
print(f'A ctps é {trabalhador["ctps"]}')

if trabalhador['ctps'] != 0:
    print(f'Contratação foi em: {trabalhador["contratação"]}')
    print(f'Salário é de: {trabalhador["salário"]}')
    trabalhador['Aposentadoria'] = (trabalhador['contratação'] + 35) - trabalhador['nascimento']
    print(f'Aposentadoria é com {trabalhador["Aposentadoria"]} anos')

'''


#Versão do professor

from datetime import date


trabalhador = dict()

atual = date.today().year

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho: '))
trabalhador['idade'] = atual - trabalhador['nascimento']

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = int(input('Salário: '))
    trabalhador['Aposentadoria'] = (trabalhador['contratação'] + 35) - trabalhador['nascimento']


#Com o metodo items() o for transforma o dicionário em lista e a partir dos numeros da posição
#ele consegue enumerar as variáveis dentro da lista, para fazer o laço

for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')