# def cumprimentar(nome:str) ->str:
#     return f'Olá {nome}'
#
# print(cumprimentar('Geek'))
# print(type(cumprimentar('Geek')))
#
# def cabecalho(texto,alinhamento=True):
#     if alinhamento:
#         return f'{texto.title()}\n{'-'*len(texto)}'
#     else:
#         return f' {texto.title()} '.center(50,'#')
#
# print(cabecalho('Geek University'))
# print(cabecalho('Geek University',alinhamento=False))

# EXPLICITANDO OS TIPOS DE DADOS, CONTUDO NÃO IMPEDE QUE O PROGRAME RODE:
def cabecalho(texto: str,alinhamento: bool=True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{'-'*len(texto)}'
    else:
        return f' {texto.title()} '.center(50,'#')

print(cabecalho('Geek University'))
print(cabecalho('Geek University',alinhamento=False))

#PROGRAMA MESMO ASSIM RODA:
#print(cabecalho('Geek University',alinhamento='geek'))

# PARA TESTAR USANDO O MYPY
# Nessa caso, ao aplicar no terminal mypy _nome_do_modulo.py ele da erro nessa linha 26
# Contudo o MYPY só funciona ao usarmos o type hinting (explicitando o tipo de dado)


# CORRETO
#texto: str

# INCORRETO
#texto:str
#texto : str

# CORRETO
#) -> str

#INCORRETO
#)->str
#) ->str

# CORRETO
#alinhamento: bool = True