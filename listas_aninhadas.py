'''
Listas Aninhadas (Nested Lists)
- Algumas linguagens de proramação (C/Java) possuem uma estrutura de dados chamados arrays:
    - Unidimensionais (arrays/vetores)
    -Multidimensionais (Matrizes)

- Em python nós temos as listas
lista = [1,3.15, "oi", True]

#Exemplos
listas = [[1,2,3], [4,5,6], [7,8,9]] #Matriz 3x3
print(type(listas))
print(listas)

#Como fazemos para acessar os dados ?
print(listas[0][1]) #linha e coluna
print(listas[0][-2]) #linha e coluna

#Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(numero) for numero in lista]for lista in listas] #Sempre lê-se de trás pra frente

'''

#Outros Exemplos
#gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1,4)] for qte_lista in range(1,4)]
print(tabuleiro)

#Gerando jogadas para o jogo da velha
velha =[['X' if num % 2 ==0 else "0" for num in range(1,4)] for qt_lista in range(1,4)]
print(velha)

#Gerando valores iniciais
print([["*" for l in range(1,4)]for j in range(1,4)])