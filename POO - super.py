'''
POO - super
super() -> Super classe
'''
class Animal:
    def __init__(self,nome,especie):
        self.__nome=nome
        self.__especie = especie
    def faz_som(self,som):
        print(f'o {self.__nome} faz {som}')

class Gato(Animal):
    def __init__(self,nome,especie,raca):
        Animal.__init__(self,nome,especie)
        super().faz_som('auauau')
        # super().__init__(nome,especie)
        self.__raca = raca

felix = Gato("Felix",'Felino','Angorá')
felix.faz_som('miau')