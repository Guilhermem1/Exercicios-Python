'''
Reversed
OBS: Não confunda cm a funcao reserve() que estudamos na listas
A função reserve() só funciona em lista, já Reversed funciona em qualquer interavel
-> A funcao reversed() retorna um interavel chamado List Reverse Iterator
'''

#Exemplos
lista = [1,2,3,4,5]
res = reversed(lista)
print(res)
print(type(res))
#Convertando o interavel
#Lista
print(list(reversed(lista)))

#Tupla
print(tuple(reversed(lista)))

#set
print(set(reversed(lista)))  #OBS: Em conjuntos, nao definimos a ordem dos elementos

#Podemos iterar sobre o Reverse
for letra in reversed("Geek University"):
    print(letra, end ='')

print('\n')

#Sem usar o for
print(''.join(list(reversed("Geek University"))))

#Outro
print('Geek University'[::-1])

#Podemos fazer oreversed para um loop inverso
for n in reversed(range(0,10)):
    print(n)

#OU
for n in range(9,0,-1):
    print(n)