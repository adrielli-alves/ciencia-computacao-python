import math

#INFORMAR AS CONSTANTES
a = float(input('Digite a constante a: '))
b = float(input('Digite a constante b: '))
c = float(input('Digite a constante c: '))

#PULAR LINHA
print()

#CALCULAR DELTA
delta = (b ** 2) - (4 * a * c)
if delta < 0:
  print('esta equação não possui raízes reais')
else:
  raiz_delta = math.sqrt(delta)

  #CALCULAR AS POSSIVEIS VARIÁVEIS
  x = (- b - raiz_delta) / (2 * a)
  y = (-b + raiz_delta) / (2 * a)

  #CASOS DO DELTA
  if delta == 0:
   print('a raiz desta equação é', x)

  else:
   print('as raízes da equação são', x, 'e', y)