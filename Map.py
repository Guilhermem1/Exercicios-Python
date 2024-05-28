'''
Map
-> Com map,. fazemos mapeamento de valores para funcao

import math
def area(r):
    return math.pi * (r**2)

raios = [2,5,7,4.4,6,8.1]
#Forma comum
areas= []
for raio in raios:
    areas.append(area(raio))
print(areas)

#Forma usando Map
#Map é uma funcao que recebe dois parametros: funcao, interável. Retorna um Map object
areas2 = map(area,raios)

print(areas2)
print(type(areas2))
print(list(areas2))

#Forma 3 - Mao com lambda
print(list(map(lambda r: math.pi * (r**2),raios)))

#OBS: Após utilizar a funcao map depois da primeira utilização do resultado, ele zera
'''

#Exemplo 2
cidades = [('Berlim',29), ("Cairo",36), ("Buenos Aires",19)]

#Lambda para transformar em fahrhneit
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] +32)
print(list(map(c_para_f,cidades)))
