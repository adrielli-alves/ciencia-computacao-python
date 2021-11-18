import math

print('Olá usuário! Este programa foi feito para calcular a área de diversas figuras geométricas')
forma = int(input('Digite 1 para quadrado, 2 para retangulo, 3 para triangulo, 4 para paralelograma, 5 para trapézio, 6 para circulo, 7 para losango e 8 para poligono regular: '))

if forma == 1:
  print('Você escolheu o quadrado')
  lado = float(input('Digite o tamanho do lado do quadrado: '))
  área = lado ** 2
  print('A área do quadrado é', área)

elif forma == 2:
  print('Você escolheu o retangulo')
  base = float(input('Digite o valor da base do retangulo: '))
  altura = float(input('Digite o valor da altura do retangulo: '))
  área = base * altura
  print('A área do retangulo é', área)

elif forma == 3:
  print('Você escolheu o triangulo')
  base = float(input('Digite o valor da base do triangulo: '))
  altura = float(input('Digite o valor da altura do triangulo: '))
  área = (base * altura) / 2
  print('A área do triangulo é', área)
  
elif forma == 4:
  print('Você escolheu o paralelograma')
  base = float(input('Digite o valor da base do paralelograma: '))
  altura = float(input('Digite o valor da altura do paralelograma: '))
  área = base * altura
  print('A área do paralelograma é', área)

elif forma == 5:
  print('Você escolheu o trapezio')
  base1 = float(input('Digite o valor da base do maior do trapezio: '))
  base2 = float(input('Digite o valor da base do menor do trapezio: '))
  altura = float(input('Digite o valor da altura do trapezio: '))
  área = ((base1 + base2) / 2) * altura
  print('A área do trapezio é', área)

elif forma == 6:
  print('Você escolheu o circulo')
  raio = float(input('Digite o valor do raio do circulo: '))
  área = math.pi * (raio ** 2)
  print('A área do circulo é', área)

elif forma == 7:
  print('Você escolheu o losango')
  diagonal1 = float(input('Digite o valor da diagonal maior do losango: '))
  diagonal2 = float(input('Digite o valor da diagonal menor do losango: '))
  área = (diagonal1 * diagonal2) / 2
  print('A área do losango é', área)

elif forma == 8:
  print('Você escolheu o poligono regular')
  lados_quant = int(input('Digite a quantidade de lados: '))
  lados_taman = float(input('Digite o tamanho de um dos lados: '))
  perímetro = lados_quant * lados_taman
  apótema = float(input('Digite o valor da apótema: '))
  área = (perímetro * apótema) / 2
  print('A área do poligono regular é', área)

else:
  print('O numero selecionado não esta relacionado a nenhuma forma geométrica')