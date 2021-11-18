def primos(numero):
    if numero < 0:
        return 'Numero inválido'
    else:
        divisor = 2
        while divisor < numero:
            if numero % divisor != 0:
                divisor = divisor + 1
            else:
                return 'O número', numero, 'pode ser dividido por', divisor
        if numero == divisor:
            return 'O número', numero, 'não possui divisores'
