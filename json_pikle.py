"""
JSON e PIKLE
JSON -> JavaScript Object Notation  (Muito usador em API de empresas)
API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facevook, Youtube) e terceiros (desenvolvedores)


import json

ret = json.dumps(['produto',{"PlayStation 4": ("2TB",'Novo', 2340)}])
print(type(ret))
print(ret)


import json

class Gato:
    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
felix = Gato('Felix','Vira Lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)


# Integrando JSON com Pikle

#pip install jsonpickle

import json

import jsonpickle


class Gato:
    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
felix = Gato('Felix','Vira Lata')

ret = jsonpickle.encode(felix)
print(ret)


#Escrevendo arquivo em JSON/ Pickle

import jsonpickle
class Gato:
    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
felix = Gato('Felix','Vira Lata')

with open('felix.json','w') as arq:
    ret = jsonpickle.encode(felix)
    arq.write(ret)
"""

#Lendo arquivo em JSON/ Pickle

import jsonpickle
class Gato:
    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

with open('felix.json','r') as arq:
    conteudo = arq.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

