n = int(input('Digite um número inteiro: '))
total = 0

if n == 0:
  print(0)
else:
  while n > 0:
    anterior = n % 100
    anterior = anterior // 10
    resto = n % 10
    n = n // 100
    soma = resto + anterior
    total = soma + total


  
  print(total)
