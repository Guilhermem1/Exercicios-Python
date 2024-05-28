'''
POO - objetos
Objetos -> São instâncias de classe, ou seja, após o mapeamento de objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos
objetos/instâncias de uma classe como varíaveis do tipo definido na classe.

 Instâncias/ Objetos
lamp1 = Lampada('branca',110,60)
lamp1.ligar_desligar()
print("A lampada esta ligada ? ",lamp1.checa_lampada())
lamp1.ligar_desligar()
print("A lampada esta ligada ? ",lamp1.checa_lampada())


cc1 = ContaCorrente(5000,600)
user = Usuario("Gui",'Mont','gui@email','123')
'''
class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f"O cliente {self.__nome} diz oi")

class ContaCorrente:
    contador = 4999

    def __init__(self,limite,saldo,cliente):
        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f"O cliente é {self.__cliente._Cliente__nome}")

class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

cli1 = Cliente("Angelina Julie",'12345679-99')
cc = ContaCorrente(5000,10000,cli1)
cc.mostra_cliente()
cc._ContaCorrente__cliente.diz()