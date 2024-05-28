class Pessoa:
    def __init__(self,nome,endereco,telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def imprimir(self):
        return f'Prezado {self.__nome}, seu endereço: {self.__endereco}, telefone de contato:{self.__telefone}'

# carlos = Pessoa("carlos",'Rua 8',202245166)
# print(carlos.imprimir)

class Quadrado:
    def __init__(self,lado):
        self.__lado = lado

    def perimetro(self):
        perimet = (4*self.__lado)
        return f'O perímetro é {perimet}'

    def area(self):
        are = (self.__lado**2)
        return f'A área é {are}'

    @property
    def imprimir(self):
        return f'O resultado total é: {self.__lado**2}, com perimetro {(4*self.__lado)}'

# lad5 = Quadrado(5)
# print(lad5.perimetro())
# print(lad5.area())
# print(lad5.imprimir)

class Eletrodomestico:
    def __init__(self,ligado):
        self.__ligado = ligado

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self,novo_ligado):
        self.__ligado = novo_ligado

    def imprimir(self):
        if self.__ligado == True:
            return f'Objeto está ligado'
        else:
            return f'Objeto desligado'

# geladeira = Eletrodomestico(True)
# print(geladeira.imprimir())
#
# geladeira.ligado = False
# print(geladeira.imprimir())

class Televisor:
    def __init__(self,canal,volume):
        self.__ligado = False
        self.__canal = canal
        self.__volume = volume

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self,novo_ligado):
        if self.__ligado is False:
            self.__ligado =  True
            return self.__ligado
        else:
            return self.__ligado

    def canal_cima(self):
        if self.__canal > 0:
            self.__canal +=1
        elif self.__canal == 60:
            self.__canal == 0

    def canal_baixo(self):
        if self.__canal <= 60:
            self.__canal -=1
        elif self.__canal == 0:
            self.__canal == 60

    def volume_cima(self):
        if self.__volume >= 0 and self.__volume<101:
            self.__volume +=1

    def volume_baixo(self):
        if self.__volume <=100 and self.__volume>=0:
            self.__volume -=1

    def imprimir(self):

        if self.__ligado == True:
            if self.__canal <=60 and self.__volume<=100:
                return f'A televisão está Ligada, sintonizado no canal {self.__canal} no volume {self.__volume}'

            elif self.__canal > 60 and self.__volume > 100:
                return f'Canal e volume nao correspondentes'
            elif self.__volume > 100:
                return f'Volume não compativel'
            else:
                return f'Canal nao compativel'

        elif self.__ligado == False:
            return f'A Televisao está desligada'

# tv10 = Televisor(10,15)
# tv10.ligado = True
# print(tv10.imprimir())
#
# tv10.volume_cima()
# tv10.volume_cima()
# print(tv10.imprimir())
# print(10*'-')
#
# tv10.volume_baixo()
# print(tv10.imprimir())
# print(10*'-')
# tv10.canal_cima()
# tv10.canal_cima()
# print(tv10.imprimir())
#
# tv10.canal_baixo()
# print(tv10.imprimir())


class Microondas:
    def __init__(self):
        self.__ligada = False
        self.__porta = False

    def ligada(self):
        if self.__ligada is False and self.__porta is False:
            self.__ligada = True
            return self.__ligada
        elif self.__ligada is True and self.__porta is True:
            self.__ligada = False
            return self.__ligada
        else:
            self.__ligada = False
            return self.__ligada


    def porta(self):
        if self.__porta is False:
            self.__porta = True
            return self.__porta
        else:
            self.__porta = False
            return self.__porta

    def imprimir(self):
        if self.__ligada:
            if self.__porta:
                return f'A porta do microondas está aberta !!!'
            else:
                return f'A porta microondas está fechada, equipamento acionado'
        else:
            return f'O microondas está desligado'


# m1 = Microondas()
# print(m1.imprimir())
# m1.ligada()
# print(m1.imprimir())
# m1.ligada()
# print(m1.imprimir())
# m1.ligada()
# m1.porta()
# print(m1.imprimir())


# PARTE 2
class Equipamento:
    def __init__(self,mouse,monitor):
        self.__mouse = mouse
        self.__monitor = monitor
    @property
    def mouse(self):
        return self.__mouse

    @property
    def monitor(self):
        return self.__monitor

    @mouse.setter
    def mouse(self,novo_mouse):
        self.__mouse = novo_mouse

    @monitor.setter
    def monitor(self,novo_monitor):
        self.__monitor = novo_monitor

    def imprimir(self):
        return f'Mouse: {self.__mouse}, Monitor:{self.__monitor}'
class Computador(Equipamento):
    def __init__(self,mouse,monitor,placa,ram):
        super().__init__(mouse,monitor)
        self.__placa = placa
        self.__ram = ram

    @property
    def placa(self):
        return self.__placa
    @property
    def ram(self):
        return self.__ram

    @placa.setter
    def placa(self,novo_placa):
        self.__placa = self.__novo_placa
    @ram.setter
    def ram(self,novo_ram):
        self.__ram = self.__novo_ram

    def imprimir(self):
        return (f'O seu mouse e monitor são respectivamente: {self._Equipamento__mouse} e {self._Equipamento__monitor}'
                f' e voce possui a placa {self.__placa} e ram {self.__ram}')


class TestaEquipamento:
    def __init__(self):
        self.__e = Equipamento('Mouse mic', 'lcd')
        self.__c = Computador('Mouse mic', 'lcd', 'Intel', 'Corsai')

    def main(self):
        print(Equipamento.imprimir(self.__e))
        print(Computador.imprimir(self.__c))


# teste = TestaEquipamento()
# teste.main()

class Pessoa:
    def __init__(self,codigo,nome,idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def exibe(self,num=None):
        if num==int(1):
            print(f'{self.__codigo},{self.__nome},{self.__idade}')
        else:
            print(f'{self.__codigo}, {self.__nome}')

class TestaPessoa(Pessoa):
    pessoa1 = Pessoa(123, 'vitor', 19)
    pessoa1.exibe(0)
    pessoa1.exibe(1)
    pessoa1.exibe(2)

    def __init__(self,codigo='nao informado',nome='nao informado',idade='nao informado'):
        super().__init__(codigo,nome,idade)

    @classmethod
    def instancia(cls):
        pessoa_teste = cls(15,'feijao',1)
        return pessoa_teste

    def exibe(self,num=None):
        if num != int(1):
            print(f'codigo:{self._Pessoa__codigo}, nome: {self._Pessoa__nome}, idade: {self._Pessoa__idade}')
        else:
            print(f'codigo:{self._Pessoa__codigo}, nome: {self._Pessoa__nome}')



pessoa2 = TestaPessoa()
pessoa2.instancia().exibe()