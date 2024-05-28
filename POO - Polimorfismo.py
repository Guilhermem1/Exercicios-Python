'''
POO - Polimorfismo

Muitas formas

Quando a gente reimplementamos um método presente na classe pai em classes filhas estamos
realizando uma sobescrita de método (Overriding).

Overriding é a melhor representação do Polimorfismo
'''

class Animal(object):
    def __init__(self,nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método")
    def comer(self):
        print(f'{self.__nome} está comendo')

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala uauau')

class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def falar(self):
        print(f'{self._Animal__nome} fala miau')

class Rato(Animal):
    def __init__(self,nome):
        super().__init__(nome)

felix = Gato("felix")
felix.comer()
felix.falar()

pluto = Cachorro("pluto")
pluto.comer()
pluto.falar()

mickey = Rato("mickey")
mickey.comer()
mickey.falar()