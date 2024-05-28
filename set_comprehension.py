'''
Set Comprehension
Lista = [1,2,3,4,5]
set = {1,2,3,4,5}


'''
#Exemplos
numeros = {num for num in range(1,7)}
print(numeros)

#Outro Exemplo
numeros = {x**2 for x in range(0,10)}
print(numeros)

#Para transformar um set em um dicionário basta colocar uma chave, já que em set há apenas valor
numeros = {x: x**2 for x in range(0,10)}
print(numeros)


#relembrando que em set não há ordenação de strings e só conta uma vez cada letra
letras = {letra for letra in "Geek University"}
print(letras)
