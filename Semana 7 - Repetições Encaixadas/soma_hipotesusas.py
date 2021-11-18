import math

def hipotenusa(hip):
    cat2 = 1
    cat1 = math.sqrt((hip ** 2) - (cat2 ** 2))
    while (cat1 * 10) % 10 != 0 and cat2 < cat1 - 1:
        cat2 = cat2 + 1
        cat1 = math.sqrt((hip ** 2) - (cat2 ** 2))
    if (cat1 * 10) % 10 != 0 or cat1 <= 0:
        return False
    else:
        return True


def soma_hipotenusas(numero):
    hip = 1
    total = 0
    while hip <= numero:
        if hipotenusa(hip) == True:
            total = total + hip
            hip = hip+ 1
        else:
            hip = hip + 1
    return total
