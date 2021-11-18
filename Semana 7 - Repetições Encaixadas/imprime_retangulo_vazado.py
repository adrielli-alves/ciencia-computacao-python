largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
n = largura
while n > 0:
    print("#", end = "")
    n = n - 1
print()
altura = altura - 2
while altura > 0:
    n = 1
    while n > 0:
        print("#", end = "",)
        n = n - 1
    n = largura - 2
    while n > 0:
        print(' ', end = '')
        n = n - 1
    n = 1
    while n > 0:    
        print('#', end = '')
        n = n - 1
    altura = altura - 1
    print()
n = largura
while n > 0:
        print("#", end = "")
        n = n - 1