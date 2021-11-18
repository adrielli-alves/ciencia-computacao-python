def maior(temperatura):
    maiortemp = 0
    for comparativo in temperatura:
        if comparativo > maiortemp:
            maiortemp = comparativo
    diacerto = 0
    for dia in range(len(temperatura)):
        if temperatura[dia] == maiortemp:
            diacerto = dia + 1
    return 'A maior temperatura foi de ', maiortemp,'ºC, no dia', diacerto


def menor(temperatura):
    menortemp = 100
    for comparativo in temperatura:
        if comparativo < menortemp:
            menortemp = comparativo
    diacerto = 0
    for dia in range(len(temperatura)):
        if temperatura[dia] == menortemp:
            diacerto = dia + 1
    return 'A menor temperatura foi de ', menortemp,'ºC, no dia', diacerto
