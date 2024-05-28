menu = '''
[d] - deposito
[s] - saque
[e] - extrato
[q] - sair'''

saldo = 0
limite = 500
numero_saques = 0
Limite_saque = 3
extrato = ''

while True:
    opcao=input(menu)
    if opcao == 'd':
        valor=float(input("Valor para deposito: "))
        if valor>0:
            saldo += valor
            extrato += f'Deposito {valor:.2f}\n'

        else:
            print("Operacao inválida")

    elif opcao =='s':
        valor=float(input("Valor para saque: "))
        if valor > saldo:
            print("Operação falhou")
        elif valor > limite:
            print("Operacao falhou")

        elif numero_saques >= Limite_saque:
            print("Operacao falhou")
        elif valor>0:
            saldo -=valor
            extrato += f'Saque {valor:.2f}\n'
            numero_saques+=1

    elif opcao =='e':
        if not extrato:
            print("Nao houve movimentações")
        else:
            print(extrato)
        print(f"saldo {saldo:.2f}")
    elif opcao =='q':
        break
    else:
        print("Operacao inváldia")
