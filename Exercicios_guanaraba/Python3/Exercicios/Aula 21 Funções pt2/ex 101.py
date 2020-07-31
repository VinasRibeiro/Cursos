'''

Crie um programa que tenha uma Função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPICIONAL ou OBRIGATÒRIO nas eleições.


def voto(ano):
    #Com o import dentro da função vc ocupa menos memoria
    #A importação sai da memoria depois que a função não é mais usada
    from datetime import date

    #Ano de dentro é local desta função
    nasc = date.today().year - ano
    print(nasc)

    if nasc < 16:
        resultado = 'NEGADO'
    elif nasc >= 16 and nasc <= 17:
        resultado = 'OPCIONAL'
    elif nasc >= 18:
        resultado = 'OBRIGATÒRIO'
    return resultado



#ano de fora é global
ano = int(input('Seu ano de nascimento: '))

print(voto(ano))

'''

def voto(ano):

    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade <18 or idade > 65:
        return f'Com {idade} anos: Voto opcional.'
    else:
        return f'Com {idade} anos: Voto obrigatório.'

print(voto(1800))