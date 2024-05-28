'''
Unittest - Antes e após hooks

----
hooks- são os testes em si. Ou seja, a execução dos testes
----

setup() -> é executado antes de cada método de teste, é útil para criarmos
instâncias de objetos e outros dados;

tearDown() -> é executado ao final de cada método de teste.É útil para excluir ou fechar conexões com
banco de dados. Geralmente utilizando como conexão com banco de dados ou exemplo arquivo texto que quissesse
excluir quando finalizar os testes etc...
'''

import unittest

class ModuloTest(unittest, TestCase):
    def setUp(self):
        #Configurações do setup()
        pass

    def test_primeiro(self):
        #setUp vai confiurar antes do teste
        # tearDown() vai rodar depois do teste

    def test_primeiro(self):
        # setUp vai confiurar antes do teste
        # tearDown() vai rodar depois do teste

    def tearDown(self):
        # configurações do tearDown()
        pass