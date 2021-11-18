numero = int(input('Digite um número inteiro: '))
divisor = 2
resultado = 1

if numero == 0 or numero == 1:
  print('primo')
else:
  while divisor < numero and numero > 0 and resultado != 0:
    resultado = numero % divisor
    divisor = divisor + 1
    
    
if resultado == 0:
  print('não primo')
else:
  print('primo')
