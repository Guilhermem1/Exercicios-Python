'''
List Comprehension
-> Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável
#Sintaxe da List Comprehension
[dado for i in dado ]

#Exemplos
numeros = [1,2,3,4,5]
res = [numero * 10 for numero in numeros]
print(res)
Para entender melhor o que está acontecendo, devemos dividir a expressão em 2 partes:
-- For numero in numeros
-- numero * 10

def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]
print(res)

#List Comprehension versus Loop

# Loop
numeros = [1,2,3,4,5]
numeros_dobrado = []
for numero in numeros:
    numero = numero * 2
    numeros_dobrado.append(numero)
print(numeros_dobrado)

#List Comprehension
print([numero * 2 for numero in numeros])

'''

#Outros exemplos
#1
nome = "geek university"
print([letra.upper() for letra in nome])

#2
amigos = ['maria',"julia",'caio','felipe']
print([amigo.title() for amigo in amigos])
#OU
def caixa_alta(nome):
    nome = nome.replace(nome[0],nome[0].upper())
    return nome
print([caixa_alta(amigo) for amigo in amigos])

#3
print([numero *3 for numero in range(1,10)])

#4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

#5
print([str(numeros) for numeros in [1,2,3,4,5,6]])