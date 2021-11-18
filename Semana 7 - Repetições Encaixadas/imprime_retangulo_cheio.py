largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
n = largura
while altura > 0:
    while n > 0:
        print("#", end = "")
        n = n - 1
    print()
    altura = altura - 1
    n = largura
