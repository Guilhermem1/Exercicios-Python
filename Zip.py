'''
Zip
zip() -> cria um interavel (Zip Object) que agrega elementos de cada um dos interaveis passados como entrada
em pares

#Exemplos
lista1 = [1,2,3]
lista2 = [4,5,6]

zip1 = (zip(lista1,lista2,'abc'))
print(zip1)
print(type(zip1))

print(list(zip1))

zip1 = (zip(lista1,lista2,'abc'))
print(tuple(zip1))

zip1 = (zip(lista1,lista2))
print(dict(zip1))

zip1 = (zip(lista1,lista2,'abc'))
print(set(zip1))


#OBS: O zip() utiliza como parametro o menor tamanho em iterável. Isso significa que se estiver trabalhando
# com interaveis diferentes, irá parar quando os lementos do menor interavel acabar
lista3 = [8,9,7,6,2]
zip1 = zip(lista1,lista2,lista3)
print(list(zip1))

#Utlizando diferentes interaveis
tupla = 1,2,3,4,5
lista = [1,2,3,4,5]
dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

zt = zip(tupla,lista,dic.values())
print(list(zt))

#Lista de tuplas
dados = [(0,1), (1,2), (3,4), (4,5)]
zit = zip(*dados)  #Descompactando tuplas
print(list(zit))  #Duas lista pegando elemento por elemento
'''
#Exemplo2:
from itertools import zip_longest
list1 = [1, 2, 3]
list2 = ['a', 'b']
list3 = ['x', 'y', 'z']
combined = list(zip_longest(list1, list2, list3, fillvalue=None))
print(combined) # out: [(1, 'a', 'x'), (2, 'b', 'y'), (3, None, 'z')]




#Exemplo mais complexo
prova1 = [50, 98, 74]
prova2 = [79, 50, 22]
alunos = ['Maria',"Julia","Ana"]
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1,prova2)}
print(final)

#OU
final = zip(alunos,map(lambda nota: max(nota), zip(prova1,prova2)))
print(dict(final))
