nome = input('Digite seu nome: ')
outro = str(input('Digite outro nome: '))
nomeigual = False

while outro != "0" or not nomeigual:
  outro = (input('Digite outro nome: ')
  if nome == outro:
    nomeigual = True

if nomeigual:
  print('O nome digitado é igual ao seu')
else:
  print('Seu nome não é igual a nenhum outro')