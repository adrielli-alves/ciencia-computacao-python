quantidade = int(input("Quantos números deseja fatorar? "))
multiplicidade = 0
while quantidade > 0:
    numero = int(input("Digite o número que deseja fatorar: "))
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            numero = numero / divisor
            multiplicidade = multiplicidade + 1
            if numero % divisor != 0:
                print('multiplicidade de ', divisor, '=', multiplicidade)
        else:
            divisor = divisor + 1
            multiplicidade = 0
    print()
    quantidade = quantidade - 1
    multiplicidade = 0