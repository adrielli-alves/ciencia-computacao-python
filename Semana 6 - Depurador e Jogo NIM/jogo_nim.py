def inicio():
  print('Bem-vindo ao jogo do NIM! Escolha:')
  print()
  escolha = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
  print()
  while escolha != 1 and escolha != 2:
    escolha = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
    print()
  return escolha


def computador_escolhe_jogada (n,m):
  a = n
  if m < n:
    while (a % (m + 1) != 0):
      a -= 1
    jogada = n - a
  else:
    jogada = n
  return jogada

def usuario_escolhe_jogada (n,m):
  jogada = int(input('Quantas peças você vai tirar? '))
  while jogada <= 0 or jogada > m or  n < m:
    print()
    print('Oops! Jogada inválida! Tente de novo. ')
    print()
    jogada = int(input('Quantas peças você vai tirar? '))
    print()
  return jogada

def partida ():
  n = int(input('Quantas peças? '))
  m = int(input('Limite de peças por jogada? '))
  print()

  if (n % (m + 1) == 0):
    print('Voce começa!')
    print()
    while n != 0:
      j = usuario_escolhe_jogada(n,m)
      n -= j
      if j > 1:
        print('Voce tirou', j, 'peças.')
      if j == 1:
        print('Você tirou uma peça.')
      if n > 1:
        print('Agora restam', n, 'peças no tabuleiro.')
      if n == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
      if n == 0:
        print('Fim do jogo! Você ganhou!')
        break
      print()

      j = computador_escolhe_jogada (n,m)
      n -= j
      if j > 1:
        print('O computador tirou', j, 'peças.')
      if j == 1:
        print('O computador tirou uma peça.')
      if n > 1:
        print('Agora restam', n, 'peças no tabuleiro.')
      if n == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
      if n == 0:
        print('Fim do jogo! O computador ganhou!')
        break
      print()


  else:
    print('O computador começa!')
    print()
    while n != 0:
      j = computador_escolhe_jogada (n,m)
      n -= j
      if j > 1:
        print('O computador tirou', j, 'peças.')
      if j == 1:
        print('O computador tirou uma peça.')
      if n > 1:
        print('Agora restam', n, 'peças no tabuleiro.')
      if n == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
      if n == 0:
        print('Fim do jogo! O computador ganhou!')
        break
      print()

      j = usuario_escolhe_jogada(n,m)
      n -= j
      if j > 1:
        print('Voce tirou', j, 'peças.')
      if j == 1:
        print('Você tirou uma peça.')
      if n > 1:
        print('Agora restam', n, 'peças no tabuleiro.')
      if n == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
      if n == 0:
        print('Fim do jogo! Você ganhou!')
        break
      print()


def campeonato():
  print('**** Rodada 1 ****')
  print()
  partida()
  print()
  print('**** Rodada 2 ****')
  print()
  partida()
  print()
  print('**** Rodada 3 ****')
  print()
  partida()
  print()


##############################################################################
escolha = inicio()
if escolha == 1:
  print('Voce escolheu uma partida isolada!')
  print()
  partida()
  print('**** Final da partida isolada! ****')

else:
  print("Voce escolheu um campeonato!")
  print()
  campeonato()
  print('**** Final do campeonato! ****')
  print()
  print('Placar: Você 0 X 3 Computador')
