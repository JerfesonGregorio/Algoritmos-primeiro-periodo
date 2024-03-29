'''
A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
Entrada
A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).

Saída
A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade.
'''

""" def recolher_valores(Num1, Dum1, Num2, Dum2):
    global N1, D1, N2, D2 
    N1, D1, N2, D2 = map(int, (Num1, Dum1, Num2, Dum2))


qnt = int(input())

Num1, frc, Dum1, op, Num2, frc, Dum2 = input().split() #Utilizar op como a operação a ser efetuada

N1, D1, N2, D2 """


# 42 linhas

from fractions import Fraction

def alocar_resultados(n1, n2):
    global resultados, res
    resultados = n1 + '/' + n2 + ' = ' + str(res) + '\n' # utilizar .join() =>  resultados = ''.join([n1, '/', n2, '=', str(res), '\n'])
    
def somar(Nu1, De1, Nu2, De2):
    alocar_resultados(str(Nu1*De2 + Nu2*De1), str(De1*De2))
    return Fraction((Nu1*De2 + Nu2*De1) / (De1*De2)).limit_denominator(10000)

def subtrair(Nu1, De1, Nu2, De2):
    alocar_resultados(str(Nu1*De2 - Nu2*De1), str(De1*De2))
    return Fraction((Nu1*De2 - Nu2*De1) / (De1*De2)).limit_denominator(10000)

def multiplicar(Nu1, De1, Nu2, De2):
    alocar_resultados(str(Nu1*Nu2), str((De1*De2)))
    return Fraction(((Nu1*Nu2) / (De1*De2))).limit_denominator(10000)

def dividir(Nu1, De1, Nu2, De2):
    alocar_resultados(str(Nu1*De2), str(Nu2*De1))
    return Fraction((Nu1*De2) / (Nu2*De1)).limit_denominator(10000)

def efetuar_conta(op):
    global N1, D1, N2, D2, res
    if op == '+':
        res = somar(N1, D1, N2, D2)
    elif op == '-':
        res = subtrair(N1, D1, N2, D2)
    elif op == '*':
        res = multiplicar(N1, D1, N2, D2)
    else:
        res = dividir(N1, D1, N2, D2)

def recolher_numeros_e_operacao(stri):
    global N1, D1, N2, D2, op
    el = stri.split()
    N1 = int(el[0]); D1 = int(el[2]); N2 = int(el[4]); D2 = int(el[6]); op = el[3]
    efetuar_conta(op)

N1, D1, N2, D2, res, op, resultados = 0, 0, 0, 0, 0, '', []
qnt = int(input())

for i in range(qnt):
    texto = str(input())
    recolher_numeros_e_operacao(texto)

print(f'{resultados}')
