'''
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo assim
que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma mais geral simples é:
try:
    //execucao problematica
except:
    //o que deve ser feito em caso de problema
#Exemplo de erro genérico
#Antes
# geek()

#Depos
try:
    geek()
except:
    print("Houve erro")
#Tente rodar a funcao geek(), caso tenha erro printa a mensagem
#OBS: Tratar erro de fomra genérica, não é a melhor forma de tratar erro, e sim de forma específica

#Exemplo - Tratando erro de forma especifica
try:
    geek()
except NameError:
    print("Funcao inexistente")


#Exemplo 2 - Tratando erro de forma especifica com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f"A funcao gerou o seguinte erro: {err}")


#Podemos efetuar diversos tratamentos de erros de uma vez:
try:
    geek()
except NameError as err:
    print("Deu NameError",err)
except TypeError as erra:
    print("Deu TypeError",erra)
except:
    print("Deu um erro diferente")
'''

def pega_valor(dicionario,chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome":"Geek"}
print(pega_valor(dic,'nome'))
print(pega_valor(dic,'game'))
print(pega_valor(dic,8))
print(pega_valor(98,'nome'))