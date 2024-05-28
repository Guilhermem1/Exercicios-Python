'''
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissao de Leitura
    - Permissao de escrita

STRINGIO -> Utlizado para ler ou escrever arquivos na memoria
'''

#Primeiro fazemos o import
from io import StringIO
msg = 'Esta apenas uma string normal '

#Podemos criar um arquivo na memoria já com a string inserida ou vazia para inserir o texto depos
arquivo = StringIO(msg)
# Isso é o equivalente de:
# open with('arquivo.txt','w')

#Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

#Observe que nao foi criado um 'arquivo.txt', pois a msg foi salvo na memoria

#Inserindo outro texto e usando o cursor

arquivo.write("Mais uma frase normal por aqui ")
arquivo.seek(0)
print(arquivo.read())