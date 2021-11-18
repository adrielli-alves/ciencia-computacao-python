def fatorial (x):
  fatorial = 1
  multiplo = 2
  while multiplo <= x:
    fatorial = fatorial * multiplo
    multiplo = multiplo + 1
  return fatorial


def binomial (x,y):
  #n!/k!.(n-k)!
  binomial = (fatorial(x))/(fatorial(y) * fatorial(x - y))
  print(binomial)