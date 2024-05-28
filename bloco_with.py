'''
With
#1 - Abrir o arquivo
#2 - Manipula o arquivo
#3 - Fechar o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados sao
fechados apos o bloco with

'''
#Bloco eith - Forma pythonica
with open("texto.txt") as arquivo:
    print(arquivo.readlines())