'''
POO - Propriedades

Em lingaugens de programação como Java, ao declararmos atributos privados nas classes, costumamos
a criar métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e
setters, onde os getters retornam o valor do atributo enquanto os setters alteram o valor do mesmo.

class Conta:
    contador = 0

    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    def extrato(self):
        return f'Seu saldo é {self.__saldo} do cliente {self.__titular}'

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def set_titular(self,titular):
        self.__titular = titular
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def set_limite(self,limite):
        self.__limite = limite


conta1 = Conta("Felicity",2000,5000)
conta2 = Conta("August",3500,10000)
print(conta1.extrato())
print(conta2.extrato())
conta1.transferir(500,conta2)
print(conta1.extrato())
print(conta2.extrato())

# soma = conta1._Conta__saldo + conta2._Conta__saldo       MANEIRA ERRADA
# print(soma)

soma = conta1.get_saldo() + conta2.get_saldo()
print(soma)

print(conta1.__dict__)
conta1.set_limite(99999)
print(conta1.__dict__)
'''

class Conta:
    contador = 0

    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    def extrato(self):
        return f'Seu saldo é {self.__saldo} do cliente {self.__titular}'

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

conta1 = Conta("Felicity",2000,5000)
conta2 = Conta("August",3500,10000)
print(conta1.extrato())
print(conta2.extrato())
conta1.transferir(500,conta2)
print(conta1.extrato())
print(conta2.extrato())

# soma = conta1._Conta__saldo + conta2._Conta__saldo       MANEIRA ERRADA
# print(soma)

soma = conta1.saldo + conta2.saldo
print(soma)

print(conta1.__dict__)
conta1.limite = 87587
print(conta1.__dict__)

print(conta1.valor_total)
