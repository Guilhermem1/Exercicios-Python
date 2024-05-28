'''
Filter
->filter() serve para filtrar dados de uma determinada coleção

import statistics
# Ddos coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, -0.1]

#calculando a média dos dados utilizando a funcao mean()
media = statistics.mean(dados)

#Assim como a funcao map, a filter recebe 2 parametros: funcao, interavel
res = filter(lambda x: x>media, dados)
print(list(res))

paises = [ '', "Aregentina", '', "Brasil", "Chile", '', "Equador" ]
res = filter(None,paises)
print(list(res))
#OU
res = filter(lambda pais:len (pais)>0, paises)
print(list(res))
#OU
res = filter(lambda pais:pais != '', paises)
print(list(res))

# A diferença entre Map e Filter é:
#Map -> Reecebe dois parametros, uma funcao e um iteravel, e retorna mapeando a funcao para cada elemento de interavel
#Filter -> Recebe dois parâmetros,uma funcao e um interavel e retorna um objeto filtrando apenas os elemento de acordo
#com a funcao
# Filter () trabalha mais casos booleanos

# Exemplo mais complexo
usuario = [
    {'username': 'samuel', 'tweets':['Eu adoro bolos', "Eu adoro pizza"]},
    {'username': 'carla', 'tweets':['Eu amo cao']},
    {'username': 'jeff', 'tweets':[]},
    {'username': 'bob123', 'tweets':['Eu amo gato', "Eu amo chocolate"]},
    {'username': 'doogo', 'tweets':[]}
]

#Filtrar os usuarios que estao inativos no Twitter
inativos = list(filter(lambda usuar: len(usuar['tweets']) ==0, usuario))
print(inativos)
#OU
inativos = list(filter(lambda usuar: not usuar['tweets'], usuario))
print(inativos)
'''

#Combinando Filter e Map
nomes = ['Vanessa', 'Ana', "Ingrid"]
#Devemos criar uma lista contento "Sua instrutora é: ",desde que a cada nome tenha menos q 5 caracteres
lista = list(map(lambda name: f"Sua instrutora é {name}",filter(lambda i: len(i)<5, nomes)))
print(lista)
