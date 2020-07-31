def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i:Inicio da contagem
    :param f:Fim da contagem
    :param p:Passo da contagem
    :return:Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)