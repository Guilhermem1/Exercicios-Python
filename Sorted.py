'''
Sorted
OBS: Nao confusa com a funcao sort() que já estudamos, ele só funciona em lista.

-> Podemos utilizar Sorted() com qualquer interavel
-> O Sorted() sempre retorna a uma lista com os elementos organizados

#Exemplo
numeros =[6,1,8]
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))
print(numeros)
'''



# Exemplo de sorted  mais complexo
usuario = [
    {'username': 'samuel', 'tweets':['Eu adoro bolos', "Eu adoro pizza"]},
    {'username': 'carla', 'tweets':['Eu amo cao']},
    {'username': 'jeff', 'tweets':[], 'cor':'azul'},
    {'username': 'bob123', 'tweets':['Eu amo gato', "Eu amo chocolate"]},
    {'username': 'doogo', 'tweets':[], 'cor':'preto', 'musica':'rock'}
]

print(usuario)
#Ordenando pelo username na ordem alfabetica
print(sorted(usuario, key = lambda usuario: usuario['username'])) #Key parametro de ordenação

#Ordenando pelo numero de tweets
print(sorted(usuario, key = lambda usuario: len(usuario['tweets'])))

#Ultimo exemplo
musicas =[
    {"musica": "Californication", 'tocou': 3},
    {"musica": "Thunderstuck", 'tocou': 2},
    {"musica": "Sweet Child", 'tocou': 5},
    {"musica": "Kiss", 'tocou': 1}
]

#Ordenando dde quem menos tocou ao que mais tocou
print(sorted(musicas, key=lambda musica: musica['tocou']))

#Ordenando da mais tocada a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))