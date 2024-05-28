'''
Módulo Collection Deque
Lista de alta performance


'''
from collections import deque
#Criando deques
deq = deque("Geek")
print(deq)

#Adicionando elemento no deque
deq.append('y') #adiciona no final
deq.appendleft("H") #Adiciona no começo
print(deq)

#Removendo elemento
print(deq.pop()) #remove ultimo elemento
deq.popleft() #remove o primeiro elemento
print(deq)