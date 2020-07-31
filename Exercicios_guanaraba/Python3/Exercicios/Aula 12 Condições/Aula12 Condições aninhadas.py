nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == "Paulo":
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana CLáudia Jéssica Juliana':
#aqui foi usado um comando in que busca na string o conteudo da variavél nome.
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))