lista = []
numero = 1
while numero > 0:
    numero = int(input('Digite um número: '))
    lista.append(numero)
print()
for i in lista[-2:0:-1]:
    print(i)
print(lista[0])

