'''
POO - Herança Múltipla
Herança Múltipla é a possibilidade de uma classe herdar de múltiplas classe, fazendo com que a
classe filha herde todos os atributos e métodos de todas as classes herdadas
# OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multideriação Direta;
    - Por Multiderivação Indireta;
'''
# Exemplo 1 - Multiderivação Direta
class Base1:
    pass
class Base2:
    pass
class Base3:
    pass

class Multiderivacao(Base1,Base2,Base3):
    pass

# Exemplo 2 - Multiderivação Indireta
class Base1:
    pass
class Base2(Base1):
    pass
class Base3(Base2):
    pass
class Multiderivacao(Base3):
    pass

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
baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguin("Tux")
print(tux.andar())
print(tux.cumprimentar()) # MRO - Method Resolution Order