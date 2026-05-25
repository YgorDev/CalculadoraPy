def calcular_operação(n1, n2, operacao):
    '''
    Função para Calcular as operações matematicas

    Parametros:
    n1 = Vai pegar o primeiro valor estabelecido pelo usuario
    n2 = Vai pegar o segunddo valor estabelecido pelo usuario
    operacao =  vai pegar qual foi o tipo de operação que o usuario escolheu
    
    '''
    if operacao == 1:
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2
    elif operacao == 4:
        return n1 / n2
    elif operacao == 5:
        return n1 ** n2
    else:
        raise ValueError('Operação inválida!')
