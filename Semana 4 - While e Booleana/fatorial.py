n = int(input('Digite o valor de n: '))
anterior = n - 1

fatorial = n * anterior

if n == 0 or n == 1:
  print(1)
else:
  while anterior > 2 and n > 2:
    n = n - 2
    anterior = n - 1
    fatorial2 = n * anterior
    fatorial = fatorial * fatorial2
  print(fatorial)