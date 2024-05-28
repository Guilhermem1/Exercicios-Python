'''
POO _ Abstração e Encapsulamento
O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilzando
classes.

conta1 = Conta("Geek",150,351000)
# ESTAS LINHAS ABAIXO NAO ESTAO ACESSIVEIS, POIS AGORA ESTÁ PRIVADO
# print(conta.numero)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)

# conta1.numero = 42
# conta1.titular = "Xuxa"
# conta1.saldo = 999999
# conta1.limite = 8854164624
#
# print(conta1.__dict__)

# Contudo, o Python nao bloqueia o Name Mangling
print(conta1.__dict__)
conta1.extrato()
print(conta1._Conta__titular) # Name Mangling
conta1._Conta__titular = "Angelina"
print(conta1.__dict__)
'''

# class Conta:
#     contador = 400
#     def __init__(self,titular,saldo,limite):
#         self.numero = Conta.contador
#         self.titular = titular
#         self.saldo = saldo
#         self.limite = limite
#         Conta.contador +=1
#
#     def extrato(self):
#         print(f"O saldo de {self.titular} é de {self.saldo} com limite de {self.limite}")
#
#     def depositar(self,valor):
#         self.saldo += valor
#
#     def sacar(self,valor):
#         self.saldo -= valor
#
# conta1 = Conta("Geek",150,351000)
# print(conta1.numero)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
# # Contudo, como os atributos estão públicos, podemos facilmente altera-los
#
# conta1.numero = 42
# conta1.titular = "Xuxa"
# conta1.saldo = 999999
# conta1.limite = 8854164624
#
# print(conta1.__dict__)


#TORNANDO PRIVADO
class Conta:
    contador = 400
    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    def extrato(self):
        print(f"O saldo de {self.__titular} é de {self.__saldo} com limite de {self.__limite}")

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

# TRANSFERINDO VALORES ENTRE CONTA
conta1 = Conta("Anegelina",150,25000)
conta1.extrato()
conta2 = Conta("Felicity",300,61000)
conta2.extrato()

#Aneglina transferindo 100 reais para Felicity
valor = 100

conta2.sacar(valor)
conta1.depositar(valor)
conta1.extrato()
conta2.extrato()

# UTILIZANDO FUNCAO (JEITO CORRETO)
    def transferir(self,valor,conta_destino):
        self.__saldo -= valor

        conta_destino.__saldo += valor
conta2.transferir(100,conta1)