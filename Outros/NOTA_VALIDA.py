nota = float(input('Digite uma nota: '))
while nota < 0 or nota > 10:
	print('A nota não é valida')
	nota = float(input('Digite outra nota: '))
print('A nota é valida')