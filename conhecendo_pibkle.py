'''
Conhecendo Pibkle

Objeto Python -> Binarização
Binarização -> Objeto Python
Este processo é chamado de serialização/deserialização

#OBS: O modulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado
trabalhar com arquivos pickle vindo de outras pessoas que você não conheçã ou de fontes
desconhecidas



#FAzendo a escrita em arquivos Pickle
with open("animais.pickle",'wb') as arquivo:
    pickle.dump((felix,pluto),arquivo)

'''
import pickle
class Animal:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo')

class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando')

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo')

felix= Gato("Felix")
pluto = Cachorro("Pub")

# Fazendo leitura em arquivos Pickle
with open("animais.pickle",'rb') as arq:
    gato,cachorro = pickle.load(arq)
    print(f'O gato se chama {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro se chama {cachorro.nome}')
    cachorro.late()
    print(f'o tipo do cachorro é {type(cachorro)}')