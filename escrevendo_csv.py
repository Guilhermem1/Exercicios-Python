"""
Escrevendo arquivos em CSV

reader() -> writer()

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linh. Este método recebe uma lista

from csv import writer
with open("filmes.csv",'w',encoding='utf-8') as arq:
    escritor_csv = writer(arq)
    filme = None
    escritor_csv.writerow(['Título','Gênero',"Duração"])
    while filme!= 'sair':
        filme = input("Nome do filme: ")
        if filme!= 'sair':
            genero = input("Genero: ")
            duracao = int(input("Duraçã do filme em minutos: "))
            escritor_csv.writerow([filme,genero,duracao])
"""


#DictWriter
#OBS: As chaves do dicionario tem que ser a mesma do cabeçalho

from csv import DictWriter
with open('filmes3.csv','w',newline='') as arq:
    cabecalho = ['Título',"Genêro","Minutos"]
    escritor_csv = DictWriter(arq, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme!= 'sair':
        filme = input("Nome do filme: ")
        if filme!= 'sair':
            genero = input("Gênero: ")
            duracao = int(input("Duração em minutos: "))
            escritor_csv.writerow({"Título":filme, "Genêro":genero, "Minutos":duracao})
