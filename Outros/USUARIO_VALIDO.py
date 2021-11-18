nome = input('Digite seu nome de usuario: ')
senha = input('Digite sua senha: ')
while nome == senha:
	print('Ocorreu um erro, o nome de usuario e a senha informada são iguais, digite novamente')
	nome = input('Digite seu nome de usuario: ')
	senha = input('Digite sua senha: ')
print('O nome de usuario e a senha são validos')