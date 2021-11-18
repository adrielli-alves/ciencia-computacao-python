def primos(numero):
    if numero < 0:
        return 'Numero inválido'
    else:
        divisor = 2
        while divisor < numero:
            if numero % divisor != 0:
                divisor = divisor + 1
            else:
                return False
        if numero == divisor:
            return True


def n_primos(x):
    numero = 2
    quantidade = 0
    while numero < x:
        if primos(numero) == True:
            quantidade = quantidade + 1
            numero = numero + 1
        else:
            numero = numero + 1
    return quantidade


