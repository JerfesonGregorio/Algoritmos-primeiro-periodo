'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
'''

x = int(input())
aa, mm, dd = (x//365), ((x%365)//30), x

while dd >= 365:
    dd -= 365

while dd > 29:
    dd -= 30

print(f'{aa} ano(s)\n{mm} mes(es)\n{dd} dia(s)')
