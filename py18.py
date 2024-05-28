class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibe(self, num=None):
        if num == 1:
            print(f'Nome: {self.__nome}, Idade:{self.__idade}, Codigo: {self.__codigo}')
        else:
            print(f'Nome: {self.__nome}, Codigo: {self.__codigo}')


class TestePessoa:
    pessoa1 = Pessoa(123, 'vitor', 19)
    pessoa1.exibe()
    pessoa1.exibe(1)
    pessoa1.exibe(2)

    def __init__(self, nome='sem nome informado', idade='sem idade informada', codigo='sem codigo informado'):
        self.__nome = nome
        self.__idade = idade
        self.__codigo = codigo

    @classmethod
    def instanciar(cls):
        tipo_pessoa1 = cls('vitor', 19, 122573)
        return tipo_pessoa1

    def exibe(self, num=None):
        if num == 1:
            print(f'Nome: {self.__nome}, Idade:{self.__idade}, Codigo: {self.__codigo}')
        else:
            print(f'Nome: {self.__nome}, Codigo: {self.__codigo}')


tipo_pessoa = TestePessoa()
tipo_pessoa.instanciar().exibe()