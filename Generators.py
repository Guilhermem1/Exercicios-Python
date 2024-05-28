'''
Generators
-> Generators - Tuple Comprehension


#aula anterior
# nomes = ['Carlos',"Cristiano","Clezio","Cadu","Vanessa"]
# print(any([nome[0]=="C" for nome in nomes]))

#Esse codigo pode ser feito uylizando Generators
nomes = ['Carlos',"Cristiano","Clezio","Cadu","Vanessa"]
print(any(nome[0]=="C" for nome in nomes))

#List Comprehension
res = [nome[0]=="C" for nome in nomes]
print(type(res))

#Generators
res = (nome[0]=="C" for nome in nomes)
print(res)

from sys import getsizeof
print(getsizeof("Geek")) #Mostra quantos bites está ocupando na memória
print(getsizeof("University"))
print(getsizeof(8))
print(getsizeof(81))
print(getsizeof(15851841818))
print(getsizeof(True))
'''
from sys import getsizeof

#Gerando uma lista de memoria com List Comprehension
list_comp = getsizeof([x*10 for x in range(1000)])

#Gerando uma lista de memoria com Set Comprehension
Set_comp = getsizeof({x*10 for x in range(1000)})

#Gerando uma lista de memoria com Dictionary Comprehension
Dic_comp = getsizeof({x: x*10 for x in range(1000)})

#Gerando uma lista de memoria com Generators
Generators = getsizeof(x*10 for x in range(1000))

print(f'List comprehension: {list_comp}')
print(f'Set comprehension: {Set_comp}')
print(f'Dictionary comprehension: {Dic_comp}')
print(f'Generators: {Generators}')

