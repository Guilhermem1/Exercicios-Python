'''
Modulo collection - counter (contador)

Collection -> High Perfomance Cointainer Datatype
Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collection Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como
parâmetro e como valor a quantidade de ocorrências desse elemento.

#Exemplo 1
#Pode ser qualquer interável (string,dicionario,lista,tuplas...)
lista = [1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,6,6,8,78,78,95]
res = Counter(lista)
#({1: 5, 2: 4, 3: 3, 4: 3, 6: 2, 78: 2, 5: 1, 8: 1, 95: 1}) , ou seja, para o elemento 1
# há 5 ocorrencias, para o elemento 2 apareceu 4 ocorrencias e assim vai.
print(res)

Exemplo 2
print(Counter("Geek Hamburguer"))
Counter({'e': 3, 'u': 2, 'r': 2, 'G': 1, 'k': 1, ' ': 1, 'H': 1, 'a': 1,
         'm': 1, 'b': 1, 'g': 1})


'''

from collections import Counter

texto = ('Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa.'
         ' Grosso modo, pode ser entendido texto como manifestação linguística das ideias de um autor,'
         ' que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e '
         'culturais. Seu tamanho é variável')
palavra = texto.split()
print(palavra)
res = Counter(palavra)
print(res)
j=0
for i in palavra:
    if i == 'texto':
        j = j +1
print("A palavra texto, que foi solicitado, apareceu",j,"vezes")
#Encontrando as 5 palavras mais ocorrentes no texto
print(res.most_common(5))
#Para mias utilidades fazer help(Counter)
