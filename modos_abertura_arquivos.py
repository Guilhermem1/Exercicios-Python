'''
Modos de abertura de arquivos
r -> leitura (padrao)
w -> escrita (subescreve caso o arquivo ja exista)
x -> abre para escrita somente se o arquivo nao exista. Caso o arquivo exista, FileExistsError
a -> abre para a escrita adicionando o conteudo no final do arquivo
#OBS: Abrindo no modo a, apend,caso o arquivo nao exista ele será criado. Caso contrario, ele gera um novo conteudo
no final do arquivo
+ -> Abre no modo de atualziação, leitura e escrita (Temos o controle do cursor)

https://docs.python.org/3/library/functions.html#open

# Exemplo em x
try:
    with open('university.txt','x') as arq:
        arq.write("gerando um conteudo em x")
except FileExistsError:
    print("O arquivo ja existe")

#Exemplo com arquivo a:
with open('frutas.txt','a') as arq:
    while True:
        frutas = input("Frutas que voce gosta senao sair ")
        if frutas == 'sair':
            break
        else:
            arq.write(frutas + '\n')
'''

#Adicionando no inicio do arquivo
with open("frutas.txt",'a') as arquivo:
    arquivo.seek(0)
    arquivo.write("Inicio da linha\n")
    arquivo.write("Subtopico \n")
    arquivo.write("Lista de frutas: \n")





