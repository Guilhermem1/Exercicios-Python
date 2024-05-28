'''
Utilizando Lambda
-> São funções sem nome, ou seja, funções anônimas

#Funcao em pyhton(a,b):
    return a+b

#Expressao Lambda
def funcao(x):
    return 3*x + 1

print(funcao(4))

lambda x: 3*x+1
calc =lambda x: 3*x+1
print(calc(4))

#Podemos ter expressoes lambda com multiplas entradas
nome_completo = lambda nome, sobrenome : nome.strip().title() +' ' + sobrenome.strip().title()
print(nome_completo("angelina",'JUlie     '))
print(nome_completo("    john  ","jones"))

#Podemos ter nenhuma ou varias entradas em lambda em Python
amar = lambda: "Como nao amar"
uma = lambda x: x**2
duas= lambda x,y: x**y+1
tres = lambda x,y,z: 3/(x+y) * z

print(amar())
print(uma(2))
print(duas(3,1))
print(tres(5,6,8))

#Outro exemplo
autores= ["Isaac Newton",'Julia Bernet', "Macario Melo", "Felipe amorim de Souza", "Joao C. pedreiro", "H.G herry"]

#ordenando por sobrenome
autores.sort(key = lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(autores)

'''
def funcao_quadratica(a,b,c):
    return lambda x: a*x**2 + b*x + c

teste = funcao_quadratica(1,2,3) #a=1, b=2, c=3
print(teste(0)) # x= 0
print(teste(2)) #x =2
print(teste(6)) #x=6
print(funcao_quadratica(1,2,3)(2))


