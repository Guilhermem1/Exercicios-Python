'''
Decorators com diferentes assinaturas


# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'olá meu nome é {nome}'

print(saudacao("joao"))


# Neste caso, sao dados 2 argumentos, logo dará TYPE ERRO
@gritar
def ordenar(principal,acompanhar):
    return f'Olá, eu gostaria de {principal} acomponhado com {acompanhar}'


 # CORRIGINDO:
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'olá meu nome é {nome}'



@gritar
def ordenar(principal,acompanhar):
    return f'Olá, eu gostaria de {principal} acomponhado com {acompanhar}'

@gritar
def lol():
    return 'lol'

print(saudacao("joao"))
print(ordenar("Picanha",'bata frita'))
print(lol())
'''


# Decoreators com Argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args,**kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. O primeiro argumento precisar ser {valor}'
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1,num2):
    return f'A soma é {num1 + num2}'

#Testando
print(soma_dez(10,22))  #Primeiro argumento 10, OK
print(soma_dez(1,15)) #Primeiro argumento nao é 10, ERRO
print(comida_favorita('pizza','salsicha'))
print(comida_favorita('pao','pizza'))