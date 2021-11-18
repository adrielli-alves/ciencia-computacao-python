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
  print('Delta é menor que zero')
  print('Não há raizes')
else:
  raiz_delta = math.sqrt(delta)

  #CALCULAR AS POSSIVEIS VARIÁVEIS
  x = (-b) / (2 * a)
  x1 = (- b + raiz_delta) / (2 * a)
  x2 = (-b - raiz_delta) / (2 * a)

  #CASOS DO DELTA
  if delta == 0:
   print('Delta é igual a zero')
   print('Só há uma raiz')
   print('raix =', x)

  else:
   print('Delta é maior que zero')
   print('Há duas raizes')
   print('raiz 1 =', x1)
   print('raiz 2 =', x2)
