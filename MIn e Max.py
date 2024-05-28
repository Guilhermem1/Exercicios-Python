'''
Min e Max
max() -> Retorna o maior valor em um interavel ou o maior de dois ou mais elementos

#exemplos
lista = [1,6,8,16,9,81,2]
print(max(lista))
print(min(lista))

dicionario ={'a':1, 'b':2, 'c':3, 'd':44, 'e':5}
print(max(dicionario))  #retorna a chave do maior valor
print(max(dicionario.values()))

'''
nomes = ["Tim", "Arthur","Oliverandozuch", "Keiran"]

print(max(nomes)) #Neste caso está pegando na ordem alfabetica
print(min(nomes))

print(max(nomes, key= lambda nome: len(nome))) #Neste caso ele já esta pegando o tamanho
print(min(nomes, key= lambda nome: len(nome)))

musicas =[
    {"musica": "Californication", 'tocou': 3},
    {"musica": "Thunderstuck", 'tocou': 2},
    {"musica": "Sweet Child", 'tocou': 5},
    {"musica": "Kiss", 'tocou': 1}
]

print(max(musicas, key = lambda musica: musica['tocou']))
print(min(musicas, key = lambda musica: musica['tocou']))

#Imprimindo somente o nome da musica

print(max['musica'])
print(min(musicas, key = lambda musica: musica['tocou'])['musica'])
print("3333333333333333")
