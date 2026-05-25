#Calculadora Basica
from function import calcular_operação
operacao = int(input('''
Escolha a operação matematica que deseja:
1 = Adição
2 = Subtração
3 = Multiplicação
4 = Divisão
5 = Exponenciação
6 = Sair
:'''))
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
resultado = calcular_operação(n1, n2, operacao)
print('=' * 30)
print('')
print(f'O resultado do calculo é {resultado}')
print('')
print('=' * 30)

    # if operacao == 1:
    #     soma = n1 + n2
    #     print(f'A soma foi de {n1} + {n2} = {soma}')
    # elif operacao == 2:
    #     subtração = n1 - n2
    #     print(f'A subtração de {n1} - {n2} = {subtração}')
    # elif operacao == 3:
    #     multiplicação = n1 * n2
    #     print(f'A multiplicação de {n1} * {n2} = {multiplicação}')
    # elif operacao == 4:
    #     divisao = n1 / n2
    #     print(f'A divisão de {n1} / {n2} = {divisao}')
    # elif operacao == 5:
    #     exponenciacao = n1 ** n2
    #     print(f'A exponenciação de {n1} ** {n2} = {exponenciacao}')
    # else:
    #     print('Programa Finalizado!')
    #     break
