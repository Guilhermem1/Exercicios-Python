'''
POO - Herança
-> reaproveitar código, mas também extender as classes
OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar
atributos e métodos da classe herdade

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matrícula;

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdade

Quando uma classe herda de outra classe, a classe herdada é conhecida como:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Clientes, Funcionarios]
    - Sub classe;
    - Classe Filha;
    - Classe Específica;
'''
class Pessoa:
    def __init__(self,nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa): #Cliente herda de Pessoa
    def __init__(self,nome,sobrenome,cpf,renda):
        super().__init__(nome,sobrenome,cpf) #super()-> pegue xxxxx da Super Classe
        # self.__nome = nome
        # self.__sobrenome = sobrenome
        # self.__cpf = cpf
        self.__renda = renda

    # def nome_completo(self):
    #     return f'{self.__nome} {self.__sobrenome}'

class Funcionario(Pessoa): #Funconario herda de Pessoa
    def __init__(self,nome,sobrenome,cpf,matricula):
        Pessoa.__init__(self,nome, sobrenome, cpf) # Forma nao comum
        # self.__nome = nome
        # self.__sobrenome = sobrenome
        # self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionario:{self._Pessoa__nome} Matricula:{self.__matricula}'

    # def nome_completo(self):
    #     return f'{self.__nome} {self.__sobrenome}'

cliente1 = Cliente('Angelina','Jolie','123456789-00',5000)
funcionario1 = Funcionario("felicity",'Jones','987654321-00',1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)