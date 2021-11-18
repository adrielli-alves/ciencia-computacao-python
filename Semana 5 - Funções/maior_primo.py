def primo (x):
  divisor = 2
  resultado = 1
  while resultado != 0 and divisor < x:
    resultado = x % divisor
    divisor += 1
  if resultado != 0:
    return True
  else:
    return False

def maior_primo (y):
  while y != 0:
    primo(y)
    if primo(y) == True:
      return y
    else:
      y -= 1
