'''
POO - Atributos
Atribuidos: Representam as caracteristicas do objeto. Pelso atributos, conseguimos representar
computacionalmente os estados de um objeto.

Em python, divimos os atributos em 3 grupos:
- Atributos em instância
- Atributos de  Classe
- Atributos dinâmicos

* Atrubutos em instância
-> São atributos declarados dentro do método construtor. O método construtor, por sua vez, é um método
especial utilizado para a construção de objetos

# Em Java seria:
public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada= false;

    public Lampada (int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em python, por convensão, foi atribuito que, todo atributo em uma classe é publico.
Ou seja, podemos ser acessado em todo o projeto
Caso queiramos demonstrar que determinado objeto deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado somente dentro da própria classe onde está declarado, utulizase __ de seu nome nome. Conhecido
como Name Mangling

# OBS: Lembre-se que isso é apenas uma convensão, ou seja, o Python não vai impedir
# que façamos acesso aos atributos sinalizados como privados fora da classe

# Exemplo:
user = Acesso('usuario@gmail.com', '12345')
print(user.email)
#print(user.__senha) #AtributeError
print(dir(user))
print(user._Acesso__senha) # Temos acesso. Mas nao deveriamos fazer esse acesso. (Name Mangling)


user.mostra_senha() # Jeito certo, pois deve estar dentro da classe
user.mostra_email()

# O que signifca atributo de instância ?
# -> Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.
user1 = Acesso('user1@gmail.com','123456')
user2 = Acesso("user2@gmail.com",'654321')
user1.mostra_email()
user2.mostra_email()
'''

# Em python, classes com Atributo de Instância Público
class Lampada:
    #metodo contrutor
    def __init__(self,voltagem,cor):
    # Nesse caso, a voltagem,cor, e ligação da lampada estao privados somente para a classe
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __int__(self,numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self,nome,descricao,valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributo privado
class Acesso:
    def __init__(self,email,senha):
        self.email = email  #publico
        self.__senha = senha #privado
    def mostra_senha (self):
        print(self.__senha)
    def mostra_email(self):
        print(self.email)

# Atributos de Classe

# Atributos de Classe são atributos que são declarados diretamente na classe, ou seja, fora do
# construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias
# da classe. Ou seja, ao invés de cada instância de classe ter seus próprios valores como é o caso dos
# atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para
# este atributo.

# refatorar classe Produto
class Produto:

    # Atributo de classe
    imposto = 1.05  #0.05% de imposto
    contador = 0

    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('playstation4','video game',2300)
p2 = Produto('Xbox S','video game',4200)

print(p1.imposto)
print(p2.imposto)
print(p1.valor)
print(p2.valor)

# OBS: Nao precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto) # Forma correta

print(p1.id)
print(p2.id)

# Atributos Dinâmico
# -> Um atributo de instância que pode ser criado em tempo de execução

#OBS: O atributo dinâmico será exclusivo da instância que o criou
prod1 = Produto('computador', 'tecnologias', 1800)
prod2 = Produto('Arroz','Mercearia',5.99)

# Criando um atributo dinâmico em tempo de execução
prod2.peso = '5kg' # Note que na classe Produto não existe o atributo peso

print(f'Nome:{prod2.nome}, Descrição:{prod2.descricao}, Valor:{prod2.valor}, Peso:{prod2.peso}')

# Deletando atributos
print(prod1.__dict__)
print(prod2.__dict__)

del prod2.peso

print(prod1.__dict__)
print(prod2.__dict__)