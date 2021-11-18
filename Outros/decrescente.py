decrescente = True
anterior = int(input('Digite o primeiro numero da sequencia: '))
proximo = int(input('Digite o próximo numero da sequencia: '))
anterior = proximo

while proximo != 0 and decrescente:
  proximo = int(input('Digite o próximo numero da sequencia: '))
  if proximo > anterior:
    decrescente = False
  anterior = proximo

if decrescente == False:
  print('A sequencia não é mais decrescente')
else:
  print('A sequencia esta em ordem decrescente')