'''
Dictionary Comprehension
Pense no seguinte:
Se quisermos criar uma lista, fazemos:
lista = [1,2,3,4,5]

Se quisermos criar uma tupla, fazemos:
tupla = (1,2,3,4,5)

Se quisermos criar um set (conjunto), fazemos:
set = {1,2,3,4,5}

Se quisermos criar um dicionário, fazemos:
dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

#Sintaxe
{chave:valor for valor in iteravel}

#Na lista era:
[valor for valor in itervel]

#Exemplo
numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado_num = {chave : valor**2 for chave,valor in numeros.items()}
print(quadrado_num)

numeros = [1,2,3,4,5,1,2]

quadrado_numeros = {valor: valor**2 for valor in numeros}
print(quadrado_numeros)

chaves = 'abcde'
valores = [1,2,3,4,5]
mistura = {chaves[i]: valores[i] for i in range(len(valores))}
print(mistura)

#Exemplo com logica condicional
numeros = [1,2,3,4,5]
res = {num : ('par' if num % 2 ==0 else 'impar') for num in numeros}
print(res)
'''
chaves = 'abcde'
valores = [1,2,3,4,5]
mistura = {chaves[i]: valores[i] for i in range(len(valores))}
print(mistura)
