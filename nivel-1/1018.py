'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

dinheiro = int(input())
valor = dinheiro
c100, c50, c20, c10, c5, c2, c1 = 0, 0, 0, 0, 0, 0, 0

while valor >= 100:
    valor -= 100
    c100 += 1

while valor >= 50:
    valor -= 50
    c50 += 1

while valor >= 20:
    valor -= 20
    c20 += 1

while valor >= 10:
    valor -= 10
    c10 += 1

while valor >= 5:
    valor -= 5
    c5 += 1

while valor >= 2:
    valor -= 2
    c2 += 1

while valor >= 1:
    valor -= 1
    c1 += 1

print(f'{dinheiro}\n{c100} nota(s) de R$ 100,00\n{c50} nota(s) de R$ 50,00\n{c20} nota(s) de R$ 20,00\n{c10} nota(s) de R$ 10,00\n{c5} nota(s) de R$ 5,00\n{c2} nota(s) de R$ 2,00\n{c1} nota(s) de R$ 1,00')