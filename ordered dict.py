'''
Modulo Collection Ordered Dict
OrderedDict -> è um diccionario que nos garante uma ordem de inserção dos elementos
'''

from collections import OrderedDict
dicionario = OrderedDict({'a':1, 'b':2, 'c':3, 'd':5})

#Dicionarios comuns a ordem nao importa
dict1 = {'a':1, 'b':2}
dict2 = {'b':2 , 'a':1}
print(dict1 == dict2)

#Ordered Dict
odict1 = OrderedDict({'a':1,'b':2})
odict2 = OrderedDict({'b':2,'a':1})
print( odict1 == odict2)