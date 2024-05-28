'''
Len, Abs, Sum , Round
#Len
-> Tamanho de um interavel
print(len("Geek University"))
print(len({1,2,3,4,5}))
print(len((1,2,3,4,5)))
print(len({'a':1,'b':2,'c':3,'d':4,'e':5}))
print(len(range(0,10)))

#Por de baixo dos panos o Python faz:
# Dunder len
print("Geek University".__len__())

#ABS
abs()
-> Retorna o módulo do valor

#SUm
sum()-> recebe um valor incial e retorna a soma dos lementos incluindo o valor inicial
OBS: O valor inicial defaul = 0
#Exemplo:
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5],5))

#Round
round() -> Retorna um valr arredondado para n digitos de precisao, senao retorna o valor inteiro mais proximo

'''
#Exemplo:
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121,2))
print(round(3.81999999999,2))

