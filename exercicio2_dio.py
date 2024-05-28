def depositar(saldo,valor,extrato,/):
	if valor > 0:
		saldo += valor
		extrato += f'Depósito: R$ {valor:.2f}\n'
		print("Deposito realziado com sucesso")
	else:
		print("Depósito mal suceidido'")
	return saldo,extrato



def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
	if valor <= saldo: # Verificar se o saque é menor que seu saldo
		saldo-=valor
		numero_saques +=1
		extrato += f'Saque R$: {valor:.2f}\n'
		print("Saque efetuado com sucesso")

	elif valor <= limite and valor>saldo: # Verificar se ele irá pedir 'empréstimo' por meio do limite
		limite = saldo + limite
		limite -= valor
		saldo = 0
		numero_saques +=1
		extrato+= f'Saque R$ {valor:.2f} com empréstimo bancário\n'
		print("Saque efetuado com sucesso")
		print("Novo limite R$",limite)
	else:
		print("Saque nao efetuado")
	if numero_saques > limite_saques:
		print("Voce nao pode mais sacar")

	return saldo,extrato,numero_saques,limite

def exibir_extrato(limite,saldo,/,*,extrato):
	print(20*"-")
	print("EXTRATO")
	if not extrato:
		print("Nao foram efetuado transições")
	else:
		print(extrato)
	print("Saldo R$ ",saldo)
	print("Limite R$",limite)
	print(20*'-')


def criar_usuario(usuarios):
	cpf=input("CPF: ")
	usuario = filtrar_usuario(cpf,usuarios)
	if usuario:
		print("Usuario ja existente")
		return menu
	nome=input("Nome do usuario: ")
	data_nascimento = input("Data de nascimento: ")
	endereco = input("Endereço: (logradouro - nº - rua - bairro - cidade/sigla do estado ")
	usuarios.append({'nome':nome, 'cpf':cpf,"data_nascimento":data_nascimento, "endereco":endereco})
	print("Usuario criado com sucesso")
def filtrar_usuario(cpf,usuarios):
	for usuario in usuarios:
		if usuario['cpf'] == cpf:
			return usuario
		else:
			return None

def criar_conta(agencia,numero_conta,usuarios):
	cpf = input("CPF: ")
	usuario = filtrar_usuario(cpf,usuarios)
	if usuario:
		print("Conta criada com sucesso")
		return {f"agencia ":agencia, 'numero_conta ':numero_conta, 'usuario ':usuario}
	print("usuario nao encontrado")

def listar_contas(contas):
	for i in contas:
		print(f'Agencia {agencia}')


menu = '''
[d] - deposito
[s] - saque
[e] - extrato
[nu] - criar novo usuario
[nc] - criar conta

[q] - sair'''

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
extrato = ''
usuarios = []
agencia = '0001'
contas = []
while True:
	opcao=input(menu)
	if opcao == 'd':
		valor = float(input("Depósito: "))
		saldo,extrato = depositar(saldo,valor,extrato)

	elif opcao =='s':
		valor = float(input("Saque: "))
		saldo,extrato,numero_saques,limite = sacar(saldo = saldo,valor = valor,extrato=extrato
							  ,limite=limite,numero_saques=numero_saques,limite_saques=limite_saques)
	elif opcao == 'e':
		exibir_extrato(limite,saldo,extrato=extrato)

	elif opcao == 'nu':
		criar_usuario(usuarios)
	elif opcao == 'nc':
		numero_conta = len(conta)+1
		conta = criar_conta(agencia,numero_conta,usuarios)
		if conta:
			contas.append(conta)








