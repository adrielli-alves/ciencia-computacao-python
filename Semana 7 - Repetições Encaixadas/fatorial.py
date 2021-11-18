quantidade = int(input('Quantos numeros deseja farotar?'))
resultado = 1
while quantidade != 0:
    digito = int(input("Digite o numero desejado: "))
    if digito < 0:
        print('Número negativo')
    else:
        while digito > 1:
            anterior = digito - 1
            salvo = digito * anterior
            digito = digito - 2
            resultado = resultado * salvo
        print(resultado)
        quantidade = quantidade - 1
        resultado = 1