# class Cadastro():
#     def __init__(self,nome,idade,altura):
#         self.__nome = nome
#         self.__idade = idade
#         self.__altura = altura
#     def MostraPessoa(self):
#         print(f"Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura}")
#
# novo = Cadastro('Joao Henrique', 21, 183)
# novo.MostraPessoa()

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura


class Agenda:
    __banco = []



    def armazena(self,pessoa):
        if len(self.__banco) < 10:
            self.__banco.append(pessoa)
            print(f'{pessoa.get_nome()} adicionado')
        else:
            print("Você passou o limite ")

    def remover(self,name):
        j=-1
        for pessoa in self.__banco:
            j+=1
            if pessoa.get_nome() == name:
                del(self.__banco[j])
                print(f'{name} removida com sucesso')
                return False
        if True:
            print("Pessoa nao encontrada")

    def listar_agenda(self):
        for pessoa in self.__banco:
            print(f'Nome: {pessoa.get_nome()}, idade {pessoa.get_idade()}, altura {pessoa.get_altura()}')

    def buscar_pessoa(self,name1):
        for pessoa in self.__banco:
            if pessoa.get_nome() == name1:
                print(f"{name1} possui o indice {self.__banco.index(pessoa)}")
                return False
        if True:
            print("Nome nao achado")

    def imprimir_por_indice(self,indice):
        if indice <= len(self.__banco):
            indic = self.__banco[indice]
            print(f"Pessoa {Pessoa.get_nome(indic)}.\nAltura {Pessoa.get_altura(indic)}.\nIdade {Pessoa.get_idade(indic)}")


p1=Pessoa('Caio',12,180)
p2=Pessoa("Juju",15,128)
p3=Pessoa("felipe",94,191)
colecao = [p1,p2,p3]

agenda = Agenda()
for pessoa in colecao:
    Agenda.armazena(agenda,pessoa)
#Listar agenda
Agenda.listar_agenda(agenda)
#
#
# #Remover
# name = input("Nome da pessoa para ser removido: ")
# Agenda.remover(agenda,name)
# Agenda.listar_agenda(agenda)
#
# #Buscar por indice
# name1 = input("Nome da pessoa a ser pesquisada para indice: ")
# Agenda.buscar_pessoa(agenda,name1)
#
# #indice
# indice = int(input("Informe o indice: "))
# Agenda.imprimir_por_indice(agenda,indice)