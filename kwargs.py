'''
**kwargs
Este difere do *args que coloca os valores extras em uma tupla, o **kwargs exige
que utilizamos parâmetros nomeados, e transforma esses parametros extras
em um dicionário.

#Exemplo
def cores_fav(**kwargs):
    for pessoa, cores in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cores}')
cores_fav(marcos='azul', fernanda='verde', estefanie = 'preto')
cores_fav()

#OBS: os parametros kward e args nao sao obrigatorios

#EXEmplo 2
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return "Voce recebeu um cumprimento Pythonico"
    elif 'geek' in kwargs:
        return f'{kwargs['geek']} Geek'
    return "Nao sei quem eh voce"

print(cumprimento_especial())
print(cumprimento_especial(geek='Python', university='Oi'))
print(cumprimento_especial(geek="assembly"))
print(cumprimento_especial(geek='especial'))
print(cumprimento_especial(university="Python"))

# Nas nossas funções, podemos ter (nesta ordem):
- Parâmetros obrigatórios:
-*args
- Parâmetros defalut (Não obrigatórios):
-**kwards

# Ex:
def minha_funcao(idade, nome, *args, solteiro=False, **kwards):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(kwards)

minha_funcao(0, "Julia")  # Apenas idade,nome
minha_funcao(34, "jao", 4, 5, 3, solteiro=True)  # nome,idade,args,solteiro
minha_funcao(18, 'Le', eu="nao", voce="vai")  # idade,nome,kwards
minha_funcao(15, 'Jotape', 9, 15, 8, java=False, Python=True)

#Importancia de manter as ordens de parametros
#Funcao com a ordem correta
# def mostra_info(a,b, *args, instrutor = "Geek", **kwards):
#     return [a,b,args,instrutor,kwards]

#Funcao com a ordem incorreta
def mostra_info(a,b, instrutor = "Geek",*args, **kwards):
    return [a,b,args,instrutor,kwards]

    def mostrar_nomes(**kwards):
    return f'{kwards['nome']} {kwards['sobrenome']}'

pessoa = {'nome': "Guilherme", 'sobrenome': "Monteiro"}

#** Desempacota o dicionario
print(mostrar_nomes(**pessoa))

'''

def soma_num(a,b,c,**kwards):
    print(a+b+c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
dicionario = dict(a=1,b=2,c=3)

soma_num(*lista)
soma_num(*tupla)
soma_num(*conjunto)
soma_num(**dicionario)
soma_num(**dicionario,len="Python")

