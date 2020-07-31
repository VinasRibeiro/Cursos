Nos dicionários vc pode criar listas e substituir a posição ou no termo certo chave
que geralmente começa com 0 e até o infinito, por palavras por exemplo

    filme = {'titulo':'Star Wars','ano':1977}

    Ou seja ele cria uma lista com dois valores star war e 1997 porém a posição que seria 0 e 1 passa a ser
    titulo como posição zero e ano como posição 1

caso vc queira printar só os valores ou conteudo das variáveis da lista vc usa.

    print(filme.values())

    assim ele vai mostrar Star wars e 1997

Agora pra mostrar as chaves ou posições, parecido com o que faz o index()
vc tem que usar o

    print(filme.keys())

    assim ele vai mostrar

    titulo e ano na tela


Usando o for

    for k,v in filme.items():
        print('O {k} é {v}')

    assim ele faz o mesmo que com uma lista normal porém na variável v que seria a posição
    ele vai inserir as chaves.

    O resultado disso seria

    O titulo é star wars
    O ano é 1997


vc pode atribuir com append um dicionário a uma lista
por exemplo na posição 0 da lista tem titulo e  starwars

ex:
print(locadora[0]['ano'])

ele pega a posição 0 e vai escrever titulo starwars


del
    O comando del é usado para apagar um setor do dicionário

EX:
    del locadora['ano']
Ele apaga a chave ano junto com o conteudo que é 1977, restando somente o titulo com o conteudo starwars

nos dicionários vc pode usar o simbolo de = para atribuir um valor.

EX:
    locadora['titulo']='ET'
    assim vc subistitui o conteudo starwars pela palavra ET
    o mesmo ocorre com numeros
    locadora['ano']=1990
    e etc...

Ex de código

estado= dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


metodo copy()
Ele é usado para copiar dicionários em uma lista

EX:
galera = list()
pessoas = dict()

galera.append(pessoas.copy())

assim ele copia um dicionario para dentro de uma posição da lista


pessoas.clear()

clear()
Serve para apagar os dados daquela lista
Assim quando vc usar loop para adicionar em outra lista os dados
são zerados antes de renovar com novos dados.


enumerate()

O enumerate gera uma tupla e atribui o valor de posição na primeira variável e o conteudo
daquela posição em outra variável

assim usando no for ele fica mais simples de usar, quando vc quer
especificar a posição e os valores correspondentes