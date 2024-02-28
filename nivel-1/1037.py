numero = float(input())

def definir_intervalo(numero):
    if numero >= 0 and numero <= 25:
        return 'Intervalo (0,25]'
    elif numero > 25 and numero <= 50:
        return 'Intervalo (25,50]'
    elif numero > 50 and numero <= 75:
        return 'Intervalo (50,75]'
    elif numero > 75 and numero <= 100:
        return 'Intervalo (75,100]'
    else:
        return 'Fora de intervalo'
        
print(definir_intervalo(numero))
