'''
Modulo Collection - Named Tuple
#recap
tupla = (1,2,3)
tupla[1]

Named tupla -> São tuplas diferenciadas onde especificamos um nome para a mesma e parâmetros

'''

from collections import namedtuple
#Precisamos definir nomes e parâmetros
#Forma 1 - Declaração de Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2 - Declaração de Named Tuple
cachorro = namedtuple('cachorro','idade, raca, nome')

#Forma 3 - Declaração de Named Tuple
cachorro = namedtuple('cachorro',['idade', 'raca', 'nome'])

#USANDO
ray = cachorro(idade = 2, raca='Chow-Chow', nome ='Ray')
print(ray)

#Acessando dados
#Forma 1
print(ray[0]) #idade

#Forma 2
print(ray.idade) #idade

print(ray.index("Chow-Chow"))
print(ray.count('Chow-Chow'))

