import math

def circunferencia(raio: float) -> float:
    return 2*math.pi*raio

print(circunferencia.__annotations__)

nome: str = 'Geej Universuty'
peso: float = 67.9
ativo: bool = True
print(__annotations__)

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'

p= Pessoa(nome='Geek Univeristy',idade=27,peso=64.5)

print(p.__dict__)
#print(p.__annotations__) nao tem annotatios
print(p.andar.__annotations__)
print(p.__init__.__annotations__)