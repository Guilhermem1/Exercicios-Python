'''
POO - Métodos
 - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto
pode realizar no seu sistema

Em python, divimos os métodos em instância e em classe

# Método de Instância
# O método dunder init __init__ é um método especial chamado de construtor e sua funcao é construir
o objeto a partir de classe.

#OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

#OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos
ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando dunder, isso não é recomendado


p1 = Produto('PS4','Video Game',2300)
print(p1.desconto(15))
print(Produto.desconto(p1, 15))

user1 = Usuario('Angelina','Julie','angelina@gmail.com','123456')
user2= Usuario("Felicity",'Jones','felicity@outlook.com','654321')

print(user1.nome_completo())
print(user2.nome_completo())

print(Usuario.nome_completo(user1))
'''

class Produto:
    contador = 0

    def __init__(self,nome,descricao,valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self,porcentagem):
        return (self.__valor * (100 - porcentagem)/100)

#pip install passlib
from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #criptografando senha
#self.__senha = cryp.encrypt(senha, rounds = 200000 , salt_size= 16) #Embaralheamento #DeprecationWarming (Desatualizado)
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

# nome = input('Nome: ')
# sobrenome = input("Sobrenome: ")
# email = input("email: ")
# senha=input("senha: ")
# confirma_senha = input("Confirme a senha: ")
#
# if senha == confirma_senha:
#     user = Usuario(nome,sobrenome,email,senha)
# else:
#     print("Senha nao conferida")
#     exit(1)
#
# print("Usuario criado com sucesso")
#
# senha = input("Informe a senha digitada: ")
# if user.checa_senha(senha):
#     print("Acesso permitido")
# else:
#     print("Acesso negado")
#
# print("Senha criptografada: ",user._Usuario__senha) # Acesso errado




# Método de Classe

from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    contador = 0
    # Método de classe ou Método Estático
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios cadastrados') #cls.contador == Usuario.contador; cls == clase

    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #criptografando senha
#self.__senha = cryp.encrypt(senha, rounds = 200000 , salt_size= 16) #Embaralheamento #DeprecationWarming (Desatualizado)
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

user = Usuario('Felicity','Jones','felicity@gmail.com','12345')

Usuario.conta_usuario() # Forma correta
user.conta_usuario() # Possível, mas incorreto



# Gerando uma instãncia privada
from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    contador = 0
    # Método de classe ou Método Estático em Java
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios cadastrados') #cls.contador == Usuario.contador; cls == clase

    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #criptografando senha
#self.__senha = cryp.encrypt(senha, rounds = 200000 , salt_size= 16) #Embaralheamento #DeprecationWarming (Desatualizado)
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print("Usuario criado: ",self.__gera_usuario())

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):  # __ significa privado
        return self.__email.split('@')[0]

user = Usuario("Angelina",'Julie',"angelina@gmail.com",'54210')

#print(user.__gera_usuario()) #AttributeError
print(user._Usuario__gera_usuario()) # Acesso de forma errada




# Método Estático em Python
from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    contador = 0
    # Método de classe ou Método Estático em Java
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios cadastrados') #cls.contador == Usuario.contador; cls == clase

    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #criptografando senha
#self.__senha = cryp.encrypt(senha, rounds = 200000 , salt_size= 16) #Embaralheamento #DeprecationWarming (Desatualizado)
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print("Usuario criado: ",self.__gera_usuario())

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):  # __ significa privado
        return self.__email.split('@')[0]

    # Método Estático em Python
    @staticmethod
    def definicao():
        return "UXR344"

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario("Guilherme",'Mariano',"guilherme@gmail.com",'5222')

print(user.contador)
print(user.definicao())