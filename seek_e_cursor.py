'''
Seek e cursors

seek() -> é utilizado para movimentar o cursor no arquivo

arquivo  =open('texto.txt')
print(arquivo.read())

#Uma vez aberto, caso o texto tenha sido reescrito, é necessario abrir novamente para atualizalo
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(20)
print(arquivo.read())

arquivo  =open('texto.txt')
# readline() -> funco que ler o arquivo linha a linha
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

arquivo  =open('texto.txt')
# readlineS()
print(len(arquivo.readlines()))
print(arquivo.readlines())
print(type(arquivo.readlines()))


#1 - Abrindo arquivo
arquivo  =open('texto.txt')

#2 - Trabalhando o arquivo
print(arquivo.read())
print(arquivo.closed) #Verifica se o arquivo está fechado ou aberto

# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)

#OBS: Teremos um ValueError após tentar manipular o arquivo sendo que ele está fechado
'''


arquivo  =open('texto.txt')
# A funcao read() podemos limitar a quantidade de carcateres a serem lidos
print(arquivo.read(50))

