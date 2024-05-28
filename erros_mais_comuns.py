'''
Erros mais comuns
è importante aprestar atenção e aprender a ler as saídas de erros geradas
-
Os erros masi comuns:
1 - SyntaxError -> Erro de sintaxe. Você escreveu algo que o Python não reconhece como parte da linguagem
#Exemplo de SyntaxError:
a) def funcao:
    print("Geek")

b) None = 1
def = 1

c) Return

2 - NameError -> Ocorre quando uma variavel ou uma funcao nao foi definida
#Exemplo de NameError
a) print(geek)

b) geek()

c) a=18
if a<10:
    msg='È menor'
print(msg)

3 - TypeError -> Ocorre quando uma funcao/operação/ação é aplicada a um tipo errado.
#Exemplo de TypeError
a) print(len(5))

b)print("Geek" + [])

c) print("Geek" + 4)

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.
#Exemplo de IndexError
a) lista = ['geek']
print(lista[2])
print(lista[0][5])

5 - ValueError -> Ocorre quando uma função/operação bult-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado
#Exemplo de ValueError
a) print(int("Geek))

6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe
#Exemplo de KeyError
a) dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função
#Exemplo de AttributeError
a) tupla = (1,2,6,2)
print(tupla.sort()) #sort é somente para lista

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)
#Exemplo de IndentationError
a)
def funcao():
print("Geek")

b)
for i i =n range(10):
i=i+1
'''



