#Calculadora Basica
from function import calcular_operação

while True:
    try:
        operacao = int(input('''
Escolha a operação matemática que deseja:
1 = Adição
2 = Subtração
3 = Multiplicação
4 = Divisão
5 = Exponenciação

: '''))
        if operacao not in [1, 2, 3, 4, 5]:
            print('Escolha uma operação válida!')
            continue
        break
    except ValueError:
        print('Digite apenas números inteiros!')

# Primeiro número
while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        break

    except ValueError:
        print('Digite um número válido!')

# Segundo número
while True:
    try:
        n2 = float(input('Digite o segundo número: '))

        # Evita divisão por zero
        if operacao == 4 and n2 == 0:
            print('Não é possível dividir por zero!')
            continue
        break
    except ValueError:
        print('Digite um número válido!')
# Cálculo
try:
    resultado = calcular_operação(n1, n2, operacao)
    print('=' * 30)
    print('')
    print(f'O resultado do cálculo é {resultado:.1f}')
    print('')
    print('=' * 30)

except Exception as erro:
    print(f'Ocorreu um erro inesperado: {erro}')

   ##Esse foi a primeira versão para entender o funcionamento, apois isso foi feito a função
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
