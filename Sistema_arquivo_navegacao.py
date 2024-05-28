"""Sistema de Arquivo Navegacao

para fazer o uso de manipulação de arquivo no sistema operiacional precisa importar e fazer uso do modulo OS


#Importantando OS
import os

#getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path(caminho) absoluto
print(os.getcwd())

#Para mudar de diretorio fazemos o uso do chdir()
os.chdir('..')  #('..') significa retornar o diretorio anterior

print(os.getcwd())

#Podemos saber se um relatorio é absoluto ou relativo
print(os.path.isabs('C:\\Users\\Guilherme')) #isabs -> Is absolute ? True (sim) / False (nao), neste caso é relativo

import os

#Podemos identificar o Sistema Operacional
print(os.name)  #posix (Linux e Mac) / nt (Windows)

#Mais detalhes do Sistema Operacional
# print(os.uname())  #Para posix

import sys
print(sys.platform)


#Juntando dois ou mais diretorios
print(os.getcwd()) #C:\Users\guilh\PycharmProjects\guppe
resc = os.path.join(os.getcwd(), 'guilherme')
os.chdir(resc)  C:\Users\guilh\PycharmProjects\guppe/guilherme
print(os.getcwd())
"""

import os
 #Listar arquivos e diretoricom o listdir()
print(os.getcwd())

import os
 #Listar arquivos e diretoricom o listdir()
print(os.listdir("C:\\"))
print(os.getcwd())

#Podmos fazer o mesmo com mais detalhes atraves com o scandir()
print(list(os.scandir()))

arquivos = list(os.scandir())
print(dir(arquivos[0]))


print(arquivos[0].inode()) #Identificacao do elemento na arvore de diretorios
print(arquivos[0].is_dir()) #É um diretorio ? False
print(arquivos[0].is_file()) #É um arquivo ? True
print(arquivos[0].is_symlink()) #É um link sombolico ? False
print(arquivos[0].name) #Nome do arquivo
print(arquivos[0].path) #Caminho até o arquivo
print(arquivos[0].stat()) #Nome do arquivo

#Fechando o scandir
os.scandir().close()






