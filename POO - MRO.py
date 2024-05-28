'''
POO - MRO - Mtehod Resolution Order

-> resolução de Order de Métodos: É a order de resolução dos métodos (quem será executado primeiro)

Em python, podemos conferir o MRO, em 3 modos:
    - Via propriedades da classe __mro__
    - Via método mro()
    - Via help
'''
class Animal:
    def __init__(self,nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} animal do mar'

class Terrestre(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Pinguin(Terrestre,Aquatico):
    def __init__(self,nome):
        super().__init__(nome)

# Testando


tux = Pinguin("Tux")
print(tux.andar())
print(tux.cumprimentar()) # MRO - Method Resolution Order
'''
Pinguin(Terrestre,Aquatico)
Eu sou tux da terra!

Pinguin(Aquatico,Terrestre)
Eu sou tux do mar!
'''