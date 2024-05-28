"""
Leitura de arquivos
Para ler um arquivo utilizamos a funcao integrada open()

open() -> A forma mais simples de utilização é passado somente 1 parametro de entrada, que neste caso é o nome do
arquivo. Essa funcao retorna _io.TextIOWrapper
https://docs.python/org/3/library/functions.html#open


"""
#Exemplo
arquivo = open('texto.txt')
print(arquivo)

print(type(arquivo))
#para ler o conteudo de um arquivo, após sua abertura, devemos utilizar o modo read()

print(arquivo.read())

#OBS: O python utiliza um recurso chamador de cursor, esse cursor funciona como um cursor quando estamos
# escrevendo