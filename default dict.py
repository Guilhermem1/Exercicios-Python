'''
Modulo Collection - Default Dict
Default Dict -> Informamos um valor Default, podendo utilizar um lambda, para informarmos
valores que ainda noa foram definidos. Caso tenteamos acessar uma chave que não exista,
essa chave será criada e o um valor default será atribuida. Evita KeyError

OBS: Lambda são funções sem nomes que podem ou ão receber parãmetros de entrada e
retorna valores
'''
from collections import defaultdict
dicionario = defaultdict(lambda:0)
dicionario['curso'] = 'Python Esencial'
print(dicionario)
print(dicionario['outro'])
print(dicionario)