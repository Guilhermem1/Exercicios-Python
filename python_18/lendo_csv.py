'''
Lendo arquivo CSV
CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula
1,2,3,4,6
"geek", "university", "oi"

# Separador por ponto e vírgula
1;2;4;7

#Separador por espaco
1 2 6 4 8
"Geek" "university" "oi"

https://dados.gov.br/dataset

#Possivel de trabalhar, mas nao ideal   -> Trabalhoso
with open('lutadores.csv',encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem python possui duas formas de ler arquivo CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts

   # Reader
from csv import reader

with open("lutadores.csv",encoding='utf-8') as arq:
    leitor_csv = reader(arq)
    next(leitor_csv) # pular o cabeçalho
    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e altura de {linha[2]} centimetros')
'''

#DictReader

from csv import DictReader

with open("lutadores.csv",encoding='utf-8') as arq:
    leitor_csv = DictReader(arq)
    for linha in leitor_csv:
        #Cada linha é um OrderedDict
        print(f'{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}')


#DictReader com outro separador

from csv import DictReader

with open("lutadores.csv",encoding='utf-8') as arq:
    leitor_csv = DictReader(arq, delimiter=',')
    for linha in leitor_csv:
        #Cada linha é um OrderedDict
        print(f'{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}')


